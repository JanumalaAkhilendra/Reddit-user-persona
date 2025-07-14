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
```

2. 📦 Install Required Python Packages
Make sure you're in a virtual environment (optional but recommended), then run:

```bash
pip install -r requirements.txt
```

3. 🔑 Create a Reddit App
To access Reddit data, you'll need to create an app for credentials:

---
- Go to: https://www.reddit.com/prefs/apps

- Scroll down and click "create another app"

- Fill in the form:
  -  Name: Persona Generator
  -  Type: Script
  -  Redirect URI: http://localhost:8080

- After creation:
  -  Copy the client ID (just below the app name)
  -  Copy the secret
  -  Use a simple user agent like: user_persona_script by u/YourRedditUsername

---

4. 🔑 Get a GROQ API Key
GROQ is a free platform that provides access to open-source LLMs like LLaMA 3.

Visit: https://console.groq.com/keys

Sign in with Google or email

Create a new API key

Copy the key


5. 🧪 Create a .env File
Create a file named .env in the root of the project and paste your credentials:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=user_persona_script by u/YourRedditUsername
GROQ_API_KEY=your_groq_api_key
```

✅ Running the Script
After completing the setup:

```bash
python reddit_user_persona.py
```
You’ll be prompted to input a Reddit profile URL:

```bash
Enter Reddit profile URL: https://www.reddit.com/user/kojied/
```

---
The script will:

 - Fetch up to 100 posts and comments

 - Generate the persona via GROQ

 - Save it as: persona_output/kojied_persona.txt
---


📂 Output Example
A sample output file will look like:

markdown
```
User Persona: u/kojied

**Interests & Hobbies**:
- Frequently engages in game-related discussions (e.g., Starfield, D&D)
[Cited: https://www.reddit.com/r/gaming/comments/example123]

**Profession or Field**:
- Possibly a developer or tech enthusiast
[Cited: https://www.reddit.com/r/learnprogramming/comments/example456]

**Writing Style**:
- Analytical, sometimes humorous
...

Generated via LLaMA 3 (GROQ)
```

📁 Project Structure
```bash
reddit-user-persona/
├── reddit_user_persona.py         # Main script
├── persona_output/                # Output folder for persona files
│   ├── kojied_persona.txt
│   └── hungry_move_6603_persona.txt
├── requirements.txt               # Python dependencies
├── .env                           # Your credentials (not committed)
└── README.md                      # This file

```

✨ Author
Janumala Akhilendra
📬 GitHub: @yourusername