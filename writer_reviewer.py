import os
import time
import re
from dotenv import load_dotenv
import requests
import pyttsx3  # For optional voice narration

# === Load API Keys ===
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# === File Paths ===
input_path = "output/chapter.txt"
rewritten_path = "output/chapter_spun.txt"
version_folder = "output/versions"
os.makedirs(version_folder, exist_ok=True)

# === Read Chapter Text ===
with open(input_path, "r", encoding="utf-8") as f:
    chapter_text = f.read()

# === Common API Headers ===
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def chat_with_model(prompt, model="mistralai/mistral-7b-instruct", role="user"):
    data = {
        "model": model,
        "messages": [{"role": role, "content": prompt}]
    }
    res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    print("[🧪] Raw response:", res.text[:500])
    return res.json()["choices"][0]["message"]["content"]

# === STEP 1: AI Writer ===
print("[✍️] Spinning chapter with AI Writer...")
writer_prompt = f"""
You are an AI book writer. Rewrite (spin) the following chapter in a modern and engaging way, keeping the core essence intact.

Text:
{chapter_text}
"""
rewritten_chapter = chat_with_model(writer_prompt)
with open(rewritten_path, "w", encoding="utf-8") as f:
    f.write(rewritten_chapter)
print("[✅] Chapter rewritten and saved.")

# === STEP 2: AI Reviewer ===
print("[🧐] Reviewing with AI Reviewer...")
reviewer_prompt = f"""
You are an AI book reviewer. Provide constructive feedback to improve the rewritten chapter below.

Text:
{rewritten_chapter}
"""
review_feedback = chat_with_model(reviewer_prompt)
print("\n[📋] Review Feedback:\n", review_feedback)

# === STEP 3: AI Editor ===
print("\n[📘] Editing with AI Editor...")
editor_prompt = f"""
You are an AI book editor. Improve sentence clarity, tone, and flow for the following chapter:
{rewritten_chapter}
"""
edited_chapter = chat_with_model(editor_prompt)

# === STEP 4: AI Critic ===
print("\n[🧠] Literary Critique from AI Critic...")
critic_prompt = f"""
You are a literary critic. Analyze the writing style, plot development, and strengths/weaknesses of the chapter:
{edited_chapter}
"""
critic_feedback = chat_with_model(critic_prompt)
print("\n[🧠] Critic Feedback:\n", critic_feedback)

# === STEP 5: RL-Based Reward Scoring ===
def score_with_rl_model(text):
    score_prompt = f"Rate this chapter overall from 1 to 10. Just return a number."
    response = chat_with_model(f"{score_prompt}\n\n{text}")
    match = re.search(r"(\d+(\.\d+)?)", response)
    if match:
        return float(match.group(1))
    raise ValueError(f"No numeric score found in RL output: {response}")

print("\n[📊] Scoring with RL model...")
score = score_with_rl_model(edited_chapter)
print(f"[🏆] RL Quality Score: {score}/10")

# === STEP 6: Optional Voice Narration ===
def narrate(text):
    engine = pyttsx3.init()
    engine.say("Here is your chapter.")
    engine.say(text[:300])  # Limit narration for speed
    engine.runAndWait()

# Uncomment to enable narration
# narrate(edited_chapter)

# === STEP 7: Human-in-the-loop Edit ===
print("\n[✍️] You can now edit the rewritten chapter.")
print("→ Open 'output/chapter_spun.txt', make your changes, then press ENTER to continue.")
input()

# Save final version with timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
version_path = os.path.join(version_folder, f"chapter_v_{timestamp}.txt")
os.rename(rewritten_path, version_path)
print(f"[✅] Final version saved: {version_path}")
print("[🎉] All steps completed successfully!")