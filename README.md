<div align="center">

# 🌆 AREA NEWS 2.0

### Local Intelligence Network · Mohakhali → Dhaka → Bangladesh

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4d8,100:426dff&height=170&section=header&text=AREA%20NEWS%202.0&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=36"/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
[![Status](https://img.shields.io/badge/Status-Development-orange?style=for-the-badge)](https://github.com/NATIONVK/area-news)

**A responsive web dashboard for local news, weather and area intelligence across Bangladesh.**

</div>

---

## 🧭 What is Area News?

Area News combines local information, news discovery and weather in one mobile-friendly dashboard. Version 2.0 keeps the original Mohakhali guide and adds wider coverage.

## 🗺️ Coverage

| Scope | Purpose |
|---|---|
| 📍 Mohakhali | Original local directory and area-focused headlines |
| 🏙️ Dhaka | City-wide news and weather |
| 🇧🇩 Bangladesh | Nationwide news discovery |

## ✨ Features

- Responsive dark dashboard with cyan/blue visual identity
- Coverage selector for Mohakhali, Dhaka and Bangladesh
- News feed powered by Google News RSS discovery, with publisher/source links
- Headline search scoped to the selected coverage area
- Optional live weather through OpenWeatherMap
- Existing Mohakhali education, healthcare, transport and landmark directory retained
- Local preference persistence using browser localStorage
- PWA shell caching for quicker repeat visits
- Legacy Python terminal dashboard retained
- Automated tests and GitHub Actions CI

> News headlines link to their original publishers. Area News does not republish full articles.

## 🧱 Architecture

    Browser / PWA
       ├── Dashboard · Search · Area selector
       ├── Local preferences (localStorage)
       ▼
    FastAPI backend
       ├── /api/areas
       ├── /api/news
       ├── /api/search
       ├── /api/weather
       └── /api/health
            ├── Google News RSS
            └── OpenWeatherMap (optional key)

## 🚀 Run locally

Requires Python 3.10+.

    git clone https://github.com/NATIONVK/area-news.git
    cd area-news
    python -m venv .venv

Activate the virtual environment:

- Windows: .venv\Scripts\activate
- Linux / macOS / Termux: source .venv/bin/activate

Install and start:

    pip install -r requirements.txt
    uvicorn app:app --host 0.0.0.0 --port 8000

Open http://127.0.0.1:8000 in your browser. On Android, open the same address in your phone browser.

## 🌤️ Enable live weather

Weather is optional. Create an OpenWeatherMap API key, then set it as an environment variable. Never paste a real key into source code or commit it.

Linux / macOS / Termux:

    export OPENWEATHER_API_KEY="your_key_here"
    uvicorn app:app --host 0.0.0.0 --port 8000

Windows PowerShell:

    $env:OPENWEATHER_API_KEY="your_key_here"
    uvicorn app:app --host 0.0.0.0 --port 8000

For hosting, add OPENWEATHER_API_KEY to the provider's secret/environment settings. See .env.example.

## 🧪 Tests

    python -m unittest discover -s tests -v

GitHub Actions runs the test suite on pushes to main/feature branches and pull requests.

## 🔐 Security notes

- No API key is stored in the repository.
- The previously embedded weather credential has been removed from the current source. Because it was exposed in a public commit, revoke/rotate it in the OpenWeatherMap dashboard; deleting it from the latest file does not erase Git history.
- Keep real credentials in environment variables or hosting secrets.
- API requests use timeouts and return controlled errors when providers are unavailable.

## 📂 Project structure

    area-news/
    ├── app.py
    ├── mohakhali_tool.py
    ├── data/areas.json
    ├── static/index.html
    ├── static/styles.css
    ├── static/app.js
    ├── static/manifest.webmanifest
    ├── static/sw.js
    ├── tests/test_app.py
    ├── .github/workflows/ci.yml
    ├── .env.example
    ├── .gitignore
    └── requirements.txt

## 🗺️ Roadmap

- [x] Preserve Mohakhali directory and terminal tool
- [x] Responsive web dashboard
- [x] Mohakhali / Dhaka / Bangladesh coverage scopes
- [x] RSS news discovery and headline search
- [x] Optional weather integration without committed secrets
- [x] Local preference persistence and PWA shell cache
- [x] Basic tests and CI workflow
- [ ] Verified traffic and public-service alerts
- [ ] Interactive maps and saved locations
- [ ] Moderated user-submitted local updates
- [ ] Deployment and live API monitoring

## 👨‍💻 Author

**NATIONVK · Yeasien Ahmed**

[GitHub](https://github.com/NATIONVK) · [Repository](https://github.com/NATIONVK/area-news)

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:426dff,100:00d4d8&height=100&section=footer"/>
</div>
