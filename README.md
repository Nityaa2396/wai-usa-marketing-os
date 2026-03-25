# WAI USA Marketing OS

AI-powered marketing operations system for Women in AI USA. Built on Claude (Anthropic) + Streamlit.

## Modules

| Module                          | Status         | Description                                           |
| ------------------------------- | -------------- | ----------------------------------------------------- |
| Campaign Intake & Brief Builder | ✅ Live        | Turn campaign inputs into a structured brief + DOCX   |
| Partnership Copilot             | 🔜 Coming Soon | Turn a partner profile into outreach strategy + email |
| Event-to-Impact Agent           | 🔜 Coming Soon | Turn event data into a sponsor-ready impact report    |

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Nityaa2396/wai-usa-marketing-os.git
cd wai-usa-marketing-os

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. New app → connect GitHub
3. Repo: `wai-usa-marketing-os`
4. Main file: `app.py`
5. Deploy

API key is entered in the UI per session — no secrets config needed.

---

## Folder Structure

```
wai-usa-marketing-os/
├── app.py                          ← OS home (module selector)
├── requirements.txt
├── README.md
├── .gitignore
├── pages/
│   └── module1_campaign_brief.py   ← Module 1 page
└── modules/
    └── module1_campaign_brief/
        ├── brief_generator.py      ← Claude API + DOCX logic
        └── brand_voice.py          ← WAI USA brand voice fingerprint
```

---

## Stack

- Python + Streamlit
- Anthropic API (Claude)
- python-docx (DOCX generation)

Built by WAI USA Marketing Team.
