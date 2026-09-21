import feedparser
import requests

# Comprehensive information about the Mohakhali area
MOHAKHALI_INFO = {
    "name": "Mohakhali, Dhaka",
    "overview": (
        "Mohakhali is a major commercial and residential hub in Dhaka, "
        "strategically located at the intersection of Gulshan, Banani, "
        "Tejgaon, and Karwan Bazar."
    ),
    "key_spots": {
        "Educational Institutions": [
            "BRAC University",
            "Bangladesh Institute of Glass and Ceramics",
            "University of Information Technology and Sciences (UITS)",
        ],
        "Hospitals & Healthcare": [
            "Mohakhali Infectious Diseases Hospital",
            (
                "National Institute of Diseases of the Chest and Hospital"
                " (NIDCH)"
            ),
            "Dhaka Metropolitan Hospital",
            "Universal Medical College & Hospital (Ayesha Memorial)",
        ],
        "Transportation Hubs": [
            (
                "Mohakhali Bus Terminal (Major terminal for northern"
                " districts)"
            ),
            "Mohakhali Railway Crossing & Flyover",
            "Gulshan-1 & Banani Connecting Bridges",
        ],
        "Commercial & Important Landmarks": [
            "T&T Colony & Mohakhali Kitchen Market",
            "Department of Archives and Library",
            (
                "icddr,b (International Centre for Diarrhoeal Disease"
                " Research, Bangladesh)"
            ),
            "SKS Tower (Shopping Mall & Cineplex)",
        ],
    },
}

CITY = "Dhaka"
WEATHER_API_KEY = "a76c7822b7a30f62107b1355feb97d7b"


def get_weather():
  try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
      temp = data["main"]["temp"]
      desc = data["weather"][0]["description"]
      print(f"\n🌤️ Area: Mohakhali, Dhaka")
      print(f"🌡️ Temperature: {temp}°C")
      print(f"☁️ Weather: {desc.capitalize()}")
    else:
      print(
          "\n⚠️ Failed to fetch weather data. Please check response status."
      )
  except Exception as e:
    print(f"Error: {e}")


def get_news():
  print("\n📰 Latest News Headlines (Prothom Alo):")
  print("-" * 45)
  try:
    rss_url = "https://www.prothomalo.com/feed/"
    feed = feedparser.parse(rss_url)

    if feed.entries:
      for i, entry in enumerate(feed.entries[:5], 1):
        print(f"{i}. {entry.title}")
    else:
      print("⚠️ Could not load news feeds. Check your internet connection.")
  except Exception as e:
    print(f"Error: {e}")


def show_details():
  print("\n" + "=" * 50)
  print(f"📍 {MOHAKHALI_INFO['name']} - Complete Guide")
  print("=" * 50)
  print(f"📝 Overview:\n{MOHAKHALI_INFO['overview']}\n")

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
  print("=========================================")
