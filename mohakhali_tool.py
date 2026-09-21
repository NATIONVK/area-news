import json
import requests
from bs4 import BeautifulSoup

# মহাখালী এলাকার সুনির্দিষ্ট তথ্য এবং ওভারভিউ
MOHAKHALI_INFO = {
    "name": "মহাখালী (Mohakhali)",
    "overview": (
        "মহাখালী ঢাকার একটি অন্যতম গুরুত্বপূর্ণ ও ব্যস্ত বাণিজ্যিক এবং আবাসিক এলাকা। "
        "এটি গুলশান, বনানী, তেজগাঁও এবং কাওরান বাজারের সংযোগস্থলে অবস্থিত।"
    ),
    "key_spots": {
        "শিক্ষা প্রতিষ্ঠান": [
            "ব্র্যাক ইউনিভার্সিটি (BRAC University)",
            "বাংলাদেশ ইনস্টিটিউট অফ গ্লাস অ্যান্ড সিরামিকস",
            "ইউনিভার্সিটি অব ইনফরমেশন টেকনোলজি অ্যান্ড সায়েন্সেস (UITS)",
        ],
        "চিকিৎসা কেন্দ্র ও হাসপাতাল": [
            "মহাখালী সংক্রামক ব্যাধি হাসপাতাল",
            "জাতীয় বক্ষব্যাধি ইনস্টিটিউট ও হাসপাতাল",
            "ঢাকা মেট্রোপলিটন হাসপাতাল",
            "ইউনিভার্সাল মেডিকেল কলেজ ও হাসপাতাল (আয়েশা মেমোরিয়াল)",
        ],
        "যাতায়াত ও যোগাযোগ": [
            "মহাখালী বাস টার্মিনাল (উত্তরবঙ্গ ও দূরপাল্লার বাসের প্রধান কেন্দ্র)",
            "মহাখালী রেলওয়ে ক্রসিং ও ফ্লাইওভার",
            "গুলশান-১ ও বনানীর সংযোগ সেতু",
        ],
        "বাণিজ্যিক ও গুরুত্বপূর্ণ প্রতিষ্ঠান": [
            "টিঅ্যান্ডটি কলোনি ও মহাখালী বাজার",
            "আর্কাইভস ও গ্রন্থাগার অধিদপ্তর",
            "আইসিডিডিআর,বি (icddr,b)",
            "এসকেএস টাওয়ার (SKS Tower - শপিং মল ও সিনেপ্লেক্স)",
        ],
    },
}

CITY = "Dhaka"
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"  # আপনার ওপেনওয়েদার এপিআই কি এখানে দিন


def get_mohakhali_weather():
  try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=bengali"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
      temp = data["main"]["temp"]
      desc = data["weather"][0]["description"]
      print(f"🌤️ এলাকা: মহাখালী, ঢাকা")
      print(f"🌡️ তাপমাত্রা: {temp}°C")
      print(f"☁️ আবহাওয়া: {desc.capitalize()}")
    else:
      print("⚠️ আবহাওয়া তথ্য আনতে এপিআই কি (API Key) চেক করুন।")
  except Exception as e:
    print(f"ত্রুটি: {e}")


def show_mohakhali_details():
  print("\n" + "=" * 40)
  print(f"📍 {MOHAKHALI_INFO['name']} - পূর্ণাঙ্গ তথ্য নির্দেশিকা")
  print("=" * 40)
  print(f"📝 পরিচিতি:\n{MOHAKHALI_INFO['overview']}\n")

  for category, items in MOHAKHALI_INFO["key_spots"].items():
    print(f"🔹 {category}:")
    for item in items:
      print(f"   - {item}")
    print()


if __name__ == "__main__":
  print("=== 🇧🇩 মহাখালী লোকাল ইনফো ও ওয়েদার টুল ===")
  get_mohakhali_weather()
  show_mohakhali_details()
  print("=========================================")
