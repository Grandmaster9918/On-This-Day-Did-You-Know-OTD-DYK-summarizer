# WikiHighlight — AI-Powered "On This Day" & "Did You Know" Generator

**Assistive AI tools for curating Wikipedia’s main page content — built for human review, not replacement.**

WikiHighlight automatically surfaces high-quality Wikipedia articles, generates concise and verified blurbs for **On This Day (OTD)** and **Did You Know (DYK)** sections, and provides a clean review interface for editors.  

Our goal: **make it easier for trusted humans to spotlight the best of Wikipedia every day.**

---

## ✨ Features

- **Automated candidate selection**  
  Ranks articles daily by quality tier, pageviews, anniversaries, and topical diversity.

- **AI-assisted blurb generation**  
  Produces concise, neutral OTD/DYK entries with strict style and length rules.

- **Fact verification**  
  Cross-checks dates, entities, and citations against article text before surfacing.

- **Human-in-the-loop review**  
  Web dashboard to approve, edit, or regenerate blurbs before publishing.

- **Structured JSON feeds**  
  Outputs `/feed/otd.json` and `/feed/dyk.json` for easy integration into Wikimedia workflows.

---

## 🛠 Tech Stack

**Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)  
**Frontend:** [React](https://react.dev/) + Vite  
**Database:** SQLite/PostgreSQL  
**Scheduling:** APScheduler (cron-style daily jobs)  
**Data Sources:**  
- [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page) (article content, metadata)  
- [Pageviews API](https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews)  
- [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) (dates & entity properties)  

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/wikihighlight.git
cd wikihighlight

# Backend setup
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
