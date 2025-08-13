from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="WikiHighlight API",
    description="AI-powered OTD/DYK generator for Wikipedia",
    version="0.1.0"
)

# --- Data Models ---
class Blurb(BaseModel):
    id: int
    type: str   # "otd" or "dyk"
    content: str
    source_url: str
    verified: bool = False

# In-memory storage (for now)
blurbs: List[Blurb] = []

# --- Routes ---
@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "WikiHighlight API running"}

@app.get("/blurbs", response_model=List[Blurb], tags=["Blurbs"])
def get_blurbs():
    return blurbs

@app.post("/blurbs", response_model=Blurb, tags=["Blurbs"])
def add_blurb(blurb: Blurb):
    blurbs.append(blurb)
    return blurb
