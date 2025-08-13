# backend/app/main.py

from fastapi import FastAPI
import requests
import openai
import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

openai.api_key = OPENAI_API_KEY

# --- Initialize FastAPI ---
app = FastAPI(
    title="Wikipedia AI Blurb Generator",
    description="Generates 'Did You Know' (DYK) or 'On This Day' (OTD) blurbs from Wikipedia articles using OpenAI GPT.",
    version="1.0.0"
)

# --- Wikipedia Fetcher ---
def fetch_wikipedia_extract(title: str) -> str:
    """
    Fetches the plain-text extract of a Wikipedia article given its title.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": title,
        "format": "json"
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        return ""
    
    data = r.json()
    page = next(iter(data["query"]["pages"].values()))
    return page.get("extract", "")

# --- AI Summarizer ---
def generate_blurb(article_text: str, blurb_type: str) -> str:
    """
    Uses OpenAI GPT to generate a concise blurb in either 'DYK' or 'OTD' style.
    """
    prompt = (
        f"You are a Wikipedia editor. Create a single {blurb_type} style blurb "
        f"from the following article text. Keep it short, fact-focused, and "
        f"formatted in a way that could go directly on the Wikipedia main page.\n\n"
        f"Article:\n{article_text}\n\nBlurb:"
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].message["content"].strip()

# --- API Endpoint ---
@app.post("/generate_blurb")
def create_ai_blurb(title: str, blurb_type: str = "DYK"):
    """
    Generates a DYK or OTD style blurb for the given Wikipedia article title.
    """
    article_text = fetch_wikipedia_extract(title)
    if not article_text:
        return {"error": f"Article '{title}' not found or could not be fetched."}
    
    blurb = generate_blurb(article_text, blurb_type.upper())
    return {"title": title, "type": blurb_type.upper(), "blurb": blurb}

# --- Root Endpoint ---
@app.get("/")
def read_root():
    return {
        "message": "Wikipedia AI Blurb Generator API is running.",
        "usage": "POST /generate_blurb?title=ARTICLE_TITLE&blurb_type=DYK or OTD"
    }
