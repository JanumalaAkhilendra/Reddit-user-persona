import os
import re
import praw
from groq import Groq
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

# Reddit Auth
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# GROQ Auth
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_username(profile_url):
    match = re.search(r"reddit\.com/user/([^/]+)/?", profile_url)
    return match.group(1) if match else None

def fetch_user_data(username, limit=100):
    user = reddit.redditor(username)
    posts, comments = [], []

    for post in tqdm(user.submissions.new(limit=limit), desc="Fetching Posts"):
        posts.append({
            "title": post.title,
            "text": post.selftext,
            "url": f"https://www.reddit.com{post.permalink}"
        })

    for comment in tqdm(user.comments.new(limit=limit), desc="Fetching Comments"):
        comments.append({
            "text": comment.body,
            "url": f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments

def generate_user_persona(username, posts, comments):
    all_text = "\n\n".join(
        [f"Post: {p['title']}\n{p['text']}" for p in posts[:20]] +
        [f"Comment: {c['text']}" for c in comments[:20]]
    )

    prompt = f"""
Analyze the following Reddit posts and comments and generate a USER PERSONA.
Include details like:

- Name (if mentioned)
- Interests & hobbies
- Profession or field of study
- Political/ideological inclinations (if any)
- Writing style & tone
- Subreddits they engage in
- Notable personality traits

Cite relevant post/comment URLs for each trait.

Data:
{all_text}
"""

    chat_response = groq_client.chat.completions.create(
        model="llama3-70b-8192",  # ✅ Recommended and available model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1800,
    )

    return chat_response.choices[0].message.content

def save_output(username, persona_text):
    filename = f"persona_output/{username.lower()}_persona.txt"
    os.makedirs("persona_output", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"[✔] Persona saved to: {filename}")

def main():
    url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(url)

    if not username:
        print("❌ Invalid Reddit profile URL.")
        return

    print(f"[+] Extracting data for user: {username}")
    posts, comments = fetch_user_data(username)
    persona_text = generate_user_persona(username, posts, comments)
    save_output(username, persona_text)

if __name__ == "__main__":
    main()
