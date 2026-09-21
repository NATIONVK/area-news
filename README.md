<div align="center">

# 🌆 MOHAKHALI AREA NEWS

### ⚡ Smart Area Intelligence • Weather • News • Local Information

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,100:0072ff&height=180&section=header&text=MOHAKHALI%20AREA%20NEWS&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>

<br>

<a href="https://github.com/NATIONVK/area-news">
<img src="https://img.shields.io/badge/GitHub-NATIONVK%2Farea--news-181717?style=for-the-badge&logo=github"/>
</a>
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Weather-OpenWeatherMap-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/News-Prothom%20Alo-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>

<br><br>

> 🚀 **A lightweight Python-based smart dashboard for Mohakhali, Dhaka.**

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=2500&pause=800&color=00C6FF&center=true&vCenter=true&width=700&lines=Welcome+to+Mohakhali+Area+News;Live+Weather+Information;Latest+News+Headlines;Local+Area+Intelligence;Built+with+Python+%F0%9F%90%8D"/>

</div>

---

## 🧭 What is Area News?

**Area News** is a Python-powered terminal dashboard focused on **Mohakhali, Dhaka**.

The project brings several useful pieces of local information together in one place:

```text
┌──────────────────────────────────────────────┐
│              🌆 MOHAKHALI HUB                │
├──────────────────────────────────────────────┤
│                                              │
│  📍 Area Information                         │
│  🌤️  Current Weather                         │
│  📰 Latest News Headlines                    │
│  🏥 Healthcare & Hospitals                   │
│  🎓 Educational Institutions                 │
│  🚌 Transportation Hubs                     │
│  🏢 Commercial Landmarks                     │
│                                              │
└──────────────────────────────────────────────┘
```

---

## ✨ Features

### 📍 Local Area Information

The dashboard contains information about **Mohakhali, Dhaka**, including:

* 🎓 Educational Institutions
* 🏥 Hospitals & Healthcare
* 🚌 Transportation Hubs
* 🏢 Commercial Areas
* 🗺️ Important Local Landmarks

---

### 🌤️ Live Weather

Weather information is fetched from **OpenWeatherMap**.

The dashboard displays:

```text
🌤️ Area: Mohakhali, Dhaka
🌡️ Temperature: XX°C
☁️ Weather: Clear Sky
```

---

### 📰 Latest News

The project reads headlines through the **Prothom Alo RSS feed** and displays the latest available headlines directly inside the terminal.

Example:

```text
📰 Latest News Headlines (Prothom Alo)
─────────────────────────────────────────────

1. Latest headline...
2. Latest headline...
3. Latest headline...
4. Latest headline...
5. Latest headline...
```

---

## 🧠 Project Architecture

```text
                ┌─────────────────────┐
                │   MOHAKHALI TOOL    │
                └──────────┬──────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
       ┌──────────┐  ┌──────────┐  ┌──────────┐
       │   AREA   │  │ WEATHER  │  │   NEWS   │
       │   INFO   │  │   API    │  │   RSS    │
       └────┬─────┘  └────┬─────┘  └────┬─────┘
            │             │             │
            └─────────────┼─────────────┘
                          ▼
                ┌──────────────────┐
                │ TERMINAL OUTPUT  │
                └──────────────────┘
```

---

## 🛠️ Tech Stack

| Technology          | Purpose              |
| ------------------- | -------------------- |
| 🐍 Python           | Core application     |
| 🌐 Requests         | Weather API requests |
| 📰 Feedparser       | RSS news parsing     |
| ☁️ OpenWeatherMap   | Weather data         |
| 🗞️ Prothom Alo RSS | News headlines       |
| 💻 Terminal         | Dashboard interface  |

---

## 📂 Project Structure

```text
area-news/
│
├── 🐍 mohakhali_tool.py
│
└── 📄 README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NATIONVK/area-news.git
```

### 2️⃣ Enter the directory

```bash
cd area-news
```

### 3️⃣ Install dependencies

```bash
pip install requests feedparser
```

### 4️⃣ Run the tool

```bash
python mohakhali_tool.py
```

---

## 🚀 Quick Start

Run everything with:

```bash
git clone https://github.com/NATIONVK/area-news.git && cd area-news && pip install requests feedparser && python mohakhali_tool.py
```

---

## 🖥️ Example Output

```text
==================================================

        🚀 MOHAKHALI SMART TERMINAL DASHBOARD

==================================================

📍 Mohakhali, Dhaka

📝 Overview:
Mohakhali is a major commercial and residential
hub in Dhaka.

🔹 Educational Institutions:
   - BRAC University
   - Bangladesh Institute of Glass and Ceramics
   - UITS

🔹 Hospitals & Healthcare:
   - Mohakhali Infectious Diseases Hospital
   - NIDCH
   - Dhaka Metropolitan Hospital

🌤️ Area: Mohakhali, Dhaka
🌡️ Temperature: XX°C
☁️ Weather: Clear Sky

📰 Latest News Headlines
─────────────────────────────────────────────

1. Latest headline
2. Latest headline
3. Latest headline
4. Latest headline
5. Latest headline

==================================================
```

---

## 🔥 Why This Project?

```text
        INFORMATION
             │
             ▼
     ┌───────────────┐
     │  AREA + NEWS  │
     │   + WEATHER   │
     └───────┬───────┘
             │
             ▼
       ONE TERMINAL
       DASHBOARD
```

Instead of checking different sources separately, this project demonstrates how Python can combine:

**Local Information + Weather API + RSS News**

into one simple terminal experience.

---

## 🗺️ Current Coverage

<div align="center">

### 📍 MOHAKHALI • DHAKA • BANGLADESH 🇧🇩

</div>

The current project is specifically configured around **Mohakhali, Dhaka**.

---

## 🔮 Future Roadmap

```text
[✓] Mohakhali Information
[✓] Weather Integration
[✓] RSS News Integration
[✓] Terminal Dashboard

[ ] 🌍 Multiple Area Support
[ ] 🔎 News Search
[ ] 🌤️ Weather Forecast
[ ] 🚦 Traffic Information
[ ] 🚨 Local Alert System
[ ] 🗺️ Interactive Map
[ ] 📊 Area Statistics
[ ] 🔔 Notification System
[ ] 🧠 Smart News Filtering
[ ] 📱 Mobile-Friendly Interface
```

---

## 🤝 Contributing

Contributions, ideas and improvements are welcome.

```bash
# Fork
# Clone
# Create your branch
# Make your changes
# Commit
# Push
# Open a Pull Request
```

---

## ⭐ Support

If you find this project interesting:

<div align="center">

### ⭐ Star the repository

### 🍴 Fork the project

### 🛠️ Build something better

</div>

---

## 👨‍💻 Author

<div align="center">

### **NATIONVK**

<a href="https://github.com/NATIONVK">
<img src="https://img.shields.io/badge/GitHub-NATIONVK-181717?style=for-the-badge&logo=github"/>
</a>

<br><br>

**Built with 🐍 Python & ❤️ from Bangladesh 🇧🇩**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0072ff,100:00c6ff&height=120&section=footer&animation=fadeIn"/>

### `MOHAKHALI AREA NEWS`

**Local Information • Live Weather • Latest News**

</div>
