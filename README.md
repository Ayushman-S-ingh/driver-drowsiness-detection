# 🚗 Driver Drowsiness Detection System

A real-time Driver Drowsiness Detection system that monitors a driver’s eye activity using computer vision, detects drowsiness and blink patterns, triggers an alarm, and displays live status on a modern web dashboard.

---

## 📌 Overview

Driver drowsiness is a major cause of road accidents worldwide. This project aims to reduce such risks by continuously monitoring the driver through a webcam and providing real-time alerts and visual feedback when drowsiness is detected.

The system combines **Computer Vision + Backend APIs + Web Dashboard** to deliver a complete end-to-end solution.

---

## ✨ Features

- 🎥 Live webcam video streaming
- 👁️ Face and eye detection using OpenCV
- 😴 Real-time drowsiness detection
- 👀 Blink counting
- 🔔 Continuous alarm until driver wakes up
- 📊 Live status & blink count on dashboard
- 🎨 Dynamic UI (Green = Awake, Red = Drowsy)
- ⚡ Optimized for real-time performance

---

## 🧠 How It Works

1. Webcam captures live video frames
2. Face and eyes are detected using Haar Cascade classifiers
3. Eye closure duration is monitored
4. If eyes remain closed beyond a threshold → **DROWSY**
5. Alarm is triggered continuously
6. Dashboard updates status and blink count in real time

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- OpenCV
- Haar Cascade Classifiers
- SimpleAudio

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 📁 Project Structure

Driver-Drowsiness-Detection/
│
├── backend/
│ ├── app.py
│ ├── api/
│ │ └── detection_routes.py
│ ├── services/
│ │ └── drowsiness_detector.py
│ ├── models/
│ │ ├── haarcascade_frontalface_default.xml
│ │ └── haarcascade_eye.xml
│ ├── assets/
│ │ └── alarm.wav
│ ├── requirements.txt
│
├── frontend/
│ ├── templates/
│ │ └── index.html
│ └── static/
│ ├── style.css
│ └── script.js
│
├── venv/
├── README.md
└── .gitignore


---

## ▶️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/driver-drowsiness-detection.git
cd driver-drowsiness-detection

python3 -m venv venv
source venv/bin/activate

pip install -r backend/requirements.txt

python3 -m backend.app

http://127.0.0.1:5000


## 🧪 Testing

The system was tested extensively to ensure reliability and real-time performance:

- Tested using live webcam feed under different lighting conditions
- Verified accurate eye blink detection during normal driving behavior
- Verified drowsiness detection based on prolonged eye closure
- Confirmed continuous alarm activation during drowsy state
- Ensured alarm stops immediately when the driver becomes alert
- Validated real-time UI updates for status and blink count
- Tested end-to-end integration between backend APIs and frontend dashboard

---

## 🚀 Future Improvements

The system can be further enhanced with the following upgrades:

- Implement Eye Aspect Ratio (EAR) based machine learning model for higher accuracy
- Add driver face recognition to personalize monitoring
- Deploy as a mobile or cloud-based web application
- Integrate cloud notifications (SMS / Email alerts)
- Extend system for real-world vehicle integration and automation
- Improve performance using GPU acceleration or optimized ML models

---

## 👨‍💻 Author

**Ayushman Singh**  
B.Tech – Computer Science & Engineering (Data Science)  
Aspiring Software Developer  

