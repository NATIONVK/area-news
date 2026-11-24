"""Legacy Mohakhali terminal dashboard retained for compatibility.
Set OPENWEATHER_API_KEY in your environment to enable weather.
"""
import os
import feedparser
import requests

MOHAKHALI_INFO = {
    "name": "Mohakhali, Dhaka",
    "overview": "Mohakhali is a major commercial and residential hub in Dhaka, near Gulshan, Banani and Tejgaon.",
    "key_spots": {
        "Educational Institutions": ["BRAC University", "Bangladesh Institute of Glass and Ceramics", "University of Information Technology and Sciences (UITS)"],
        "Hospitals & Healthcare": ["Mohakhali Infectious Diseases Hospital", "National Institute of Diseases of the Chest and Hospital (NIDCH)", "Dhaka Metropolitan Hospital", "Universal Medical College & Hospital (Ayesha Memorial)"],
        "Transportation Hubs": ["Mohakhali Bus Terminal (Major terminal for northern districts)", "Mohakhali Railway Crossing & Flyover", "Gulshan-1 & Banani Connecting Bridges"],
        "Commercial & Important Landmarks": ["T&T Colony & Mohakhali Kitchen Market", "Department of Archives and Library", "icddr,b (International Centre for Diarrhoeal Disease Research, Bangladesh)", "SKS Tower (Shopping Mall & Cineplex)"],
    },
}
CITY = "Dhaka"

def get_weather():
    key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not key:
        print("\\n⚠️ Weather disabled: set OPENWEATHER_API_KEY in your environment.")
        return
    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather",
            params={"q": CITY, "appid": key, "units": "metric"}, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"\\n🌤️ Area: Mohakhali, Dhaka")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"☁️ Weather: {data['weather'][0]['description'].capitalize()}")
    except requests.RequestException as exc:
        print(f"⚠️ Weather service unavailable: {exc}")

def get_news():
    print("\\n📰 Latest News Headlines (Prothom Alo):")
    print("-" * 45)
    try:
        response = requests.get("https://www.prothomalo.com/feed/", timeout=12)
        response.raise_for_status()
        feed = feedparser.parse(response.content)
        if feed.entries:
            for index, entry in enumerate(feed.entries[:5], 1):
                print(f"{index}. {entry.get('title', 'Untitled')} — {entry.get('link', '')}")
        else:
            print("⚠️ No news entries are available right now.")
    except requests.RequestException as exc:
        print(f"⚠️ News feed unavailable: {exc}")

def show_details():
    print("\\n" + "=" * 50)
    print(f"📍 {MOHAKHALI_INFO['name']} - Complete Guide")
    print("=" * 50)
    print(f"📝 Overview:\\n{MOHAKHALI_INFO['overview']}\\n")
    for category, items in MOHAKHALI_INFO["key_spots"].items():
        print(f"🔹 {category}:")
        for item in items:
            print(f"   - {item}")
        print()

if __name__ == "__main__":
    print("=== 🚀 Mohakhali Smart Terminal Dashboard ===")
    show_details()
    get_weather()
    get_news()
    print("=" * 45)
