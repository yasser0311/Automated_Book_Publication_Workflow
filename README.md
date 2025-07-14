# 📚 BookFlow – Automation Book Publication Workflow. It's an AI-Powered Book Chapter Spinner with RL & Agentic Workflow

BookFlow is an intelligent automated pipeline that:

- 🔍 Scrapes book chapter content from web sources (e.g., WikiSource)
- ✍️ Spins the chapter using an **AI Writer**
- 🧐 Reviews it with an **AI Reviewer**
- 📘 Refines it using an **AI Editor**
- 🧠 Critiques it with an **AI Literary Critic**
- 📊 Scores quality using **RL-based Reward Modeling**
- 🗣️ Offers optional **voice narration**
- 👩‍💻 Supports **Human-in-the-loop** editing and version tracking

---

## 🚀 Demo

```bash
# Step 1: Scrape chapter from WikiSource
python scraper.py

# Step 2: Run the full AI + RL pipeline
python writer_reviewer.py
````

---

## 📸 Example Screenshot

The scraper pulls both **raw chapter text** and a **screenshot** of the source page.

```
output/
├── chapter.txt         # Raw scraped text
├── screenshot.png      # Page screenshot
├── chapter_spun.txt    # AI-generated rewritten chapter
├── versions/           # Timestamped final versions
```

---

## 🧠 Pipeline Agents

| Agent         | Role                                         |
| ------------- | -------------------------------------------- |
| **Writer**    | Rewrites (spins) the original text using LLM |
| **Reviewer**  | Provides feedback and suggestions            |
| **Editor**    | Applies editorial improvements (flow, tone)  |
| **Critic**    | Offers literary critique on style & story    |
| **RL Scorer** | Gives a 1–10 score using reward modeling     |
| **Narrator**  | (Optional) Reads out the rewritten chapter   |

---

## 🎯 RL-Based Reward Model

The system uses **OpenRouter-compatible models** to simulate an RL-based feedback loop. It scores rewritten chapters by asking the model to rate quality on a scale of 1 to 10. Only the numeric output is extracted and saved.

---

## 🔉 Voice Narration (Optional)

The rewritten chapter can be narrated aloud using `pyttsx3`.
Uncomment the `narrate()` function to enable text-to-speech in `writer_reviewer.py`.

---

## 🛠️ Setup

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Add `.env` File

```
OPENROUTER_API_KEY=your_api_key_here
```

Get your key from: [https://openrouter.ai](https://openrouter.ai)

---

## 🧪 Models Tested

* `mistralai/mistral-7b-instruct` ✅
* `openai/gpt-3.5-turbo` ❌ (No free endpoint currently)
* `deepinfra/...` and `enfer/...` providers work well on OpenRouter

---

## 🔐 Folder Structure

```
BookFlow/
│
├── scraper.py            # Scrapes content + screenshots
├── writer_reviewer.py    # Main multi-agent RL pipeline
├── requirements.txt
├── .env                  # Your API keys (not tracked in Git)
└── output/
    ├── chapter.txt
    ├── screenshot.png
    ├── chapter_spun.txt
    └── versions/
        └── chapter_v_*.txt
```

---

## 🧠 Tech Stack

* **Python** – core scripting
* **Playwright** – scraping + screenshots
* **Requests** – OpenRouter API calls
* **pyttsx3** – local TTS engine
* **LLMs via OpenRouter** – multi-agent persona building
* **Custom RL Parser** – score extraction from LLM responses

---

## 📜 License

MIT – You’re free to build your own AI publishing assistant on top of this project.

---

## 🙋 Author

M. Mohammed Yasser
[LinkedIn](https://www.linkedin.com/in/yasser0311) | [GitHub](https://github.com/yasser0311)

````

---

### ✅ GitHub Push Steps

If you haven't pushed the updated code yet:

```bash
git add .
git commit -m "✨ Add RL scoring, multi-agent pipeline, and voice narration to BookFlow"
git branch -M main
git remote add origin https://github.com/yasser0311/BookFlow.git  # Or your real repo URL
git push -u origin main
````
