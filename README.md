# 🧠 Reddit User Persona Generator

This project scrapes a Reddit user's posts and comments, then uses an LLM (via **GROQ API**) to generate a **detailed user persona** based on their online activity. It outputs a structured `.txt` file containing personality traits, interests, writing style, and citations of Reddit links used in the analysis.

---

## 🚀 Features

- ✅ Fetches latest Reddit posts & comments from a public user profile
- 🧠 Uses a free, fast GROQ-hosted LLM (`llama3-70b-8192`) to generate insights
- 🔍 Identifies:
  - Interests & hobbies
  - Profession or field
  - Political/social inclination
  - Tone & writing style
  - Subreddits engaged with
- 📎 Cites Reddit post/comment links used for trait extraction
- 📝 Saves a clean, readable `.txt` file for each analyzed user

---

## 📦 Tech Stack

- **Python 3.8+**
- [PRAW](https://praw.readthedocs.io/) for Reddit scraping
- [GROQ](https://console.groq.com/) LLM API
- `dotenv`, `tqdm` for environment management and UX

---

## 🔧 Setup Instructions

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-user-persona.git
cd reddit-user-persona
