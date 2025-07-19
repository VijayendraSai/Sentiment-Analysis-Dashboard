# 🧠 Full-Stack AI-Powered Sentiment Analysis Dashboard

## 📘 Overview

This project is a full-stack web application that enables users to input text and receive **AI-powered sentiment analysis**. The system provides real-time feedback on whether the sentiment is **Positive, Negative, or Neutral**, and displays the **confidence score**. A simple dashboard also displays a history of all previously analyzed texts.

---

## 🎥 Demo Video

**Demo Video**: [Watch here](https://drive.google.com/file/d/1hsyrXwxGKqVPpP0bX343a-FOX1h7Mat1/view?usp=sharing)

---

## 🚀 Features

### Frontend (React or Svelte)
- Clean and responsive UI
- Text input field for user queries
- "Analyze" button to submit text
- Real-time sentiment results display (label + confidence score)
- Dashboard showing history of analyzed texts

### Backend (Express.js or Flask/FastAPI)
- `/analyze` endpoint: Accepts text input, runs sentiment analysis, returns result
- `/history` endpoint: Returns all previously analyzed texts
- Stores history in memory or lightweight database (SQLite, MongoDB, or Redis)

### AI Integration
- Uses a sentiment analysis model (e.g., TextBlob, Hugging Face Transformers, OpenAI API)
- Classifies text into: Positive, Negative, or Neutral
- Returns label with confidence score


---

## ⚙️ Setup & Installation

### 🔹 Frontend Setup (React Example)

```bash
cd client
npm install
npm start

### 🔹 Backend Setup (Python + Flask Example)
cd server
pip install -r requirements.txt
python app.py

For Express backend, use: npm install && node index.js

