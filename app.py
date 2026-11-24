"""Area News 2.0 FastAPI backend."""
import json
import os
from pathlib import Path
from urllib.parse import quote_plus

import feedparser
import requests
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
AREAS = ROOT / "data" / "areas.json"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

app = FastAPI(title="Area News API", version="2.0.0")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


def load_areas():
    with AREAS.open(encoding="utf-8") as file:
        return json.load(file)


def get_area(area_id):
    for area in load_areas()["areas"]:
        if area["id"].lower() == area_id.lower():
            return area
    raise HTTPException(status_code=404, detail="Area not found")


def news_items(query, limit=12):
    url = "https://news.google.com/rss/search?q={}&hl=bn&gl=BD&ceid=BD:bn".format(quote_plus(query))
    try:
        response = requests.get(url, timeout=12, headers={"User-Agent": "AreaNews/2.0"})
        response.raise_for_status()
        feed = feedparser.parse(response.content)
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail="News source is temporarily unavailable.") from exc
    return [{
        "title": str(item.get("title", "Untitled")),
        "url": str(item.get("link", "")),
        "published": str(item.get("published", "")),
        "source": str(item.get("source", {}).get("title", "News")),
    } for item in feed.entries[:limit]]


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(STATIC / "index.html")


@app.get("/api/health")
def health():
    return {"status": "ok", "version": "2.0.0"}


@app.get("/api/areas")
def areas():
    return load_areas()


@app.get("/api/areas/{area_id}")
def area_details(area_id: str):
    return get_area(area_id)


@app.get("/api/news")
def news(area: str = "mohakhali", limit: int = Query(12, ge=1, le=30)):
    selected = get_area(area)
    return {"area": selected["id"], "items": news_items(selected.get("news_query", selected["name"]), limit)}


@app.get("/api/search")
def search(q: str = Query(min_length=2, max_length=80), area: str = "bangladesh"):
    selected = get_area(area)
    return {"query": q, "area": selected["id"], "items": news_items(q + " " + selected.get("news_query", selected["name"]), 15)}


@app.get("/api/weather")
def weather(area: str = "mohakhali"):
    selected = get_area(area)
    key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not key:
        return {"available": False, "area": selected["id"], "message": "Set OPENWEATHER_API_KEY to enable live weather."}
    try:
        response = requests.get(WEATHER_URL, params={
            "q": selected.get("weather_query", selected["name"]), "appid": key, "units": "metric"
        }, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail="Weather service is temporarily unavailable.") from exc
    return {
        "available": True, "area": selected["id"],
        "temperature": data.get("main", {}).get("temp"),
        "description": data.get("weather", [{}])[0].get("description", "Unknown").capitalize(),
        "humidity": data.get("main", {}).get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed"),
    }
