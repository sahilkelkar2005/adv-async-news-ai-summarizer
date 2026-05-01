# 📰 Advanced Asynchronous News AI Summarizer

An **AI-powered news summarization system** built using an **asynchronous producer–consumer architecture**.
This project demonstrates **advanced system design concepts** such as decoupled processing, multi-worker scalability, and non-blocking UI interaction.

---

## 🚀 Live Demo

👉 Add your Streamlit link here

```
https://your-streamlit-app-link
```

---

## 📌 Project Overview

This system allows users to input news text and receive an AI-generated summary.
Unlike traditional synchronous apps, this system uses an **asynchronous pipeline**:

* Requests are queued instead of processed instantly
* Worker threads handle processing independently
* UI remains responsive and non-blocking

---

## 🧠 System Architecture

```
User (UI - Streamlit)
        ↓
Task Queue (Producer)
        ↓
Worker Threads (Consumers)
        ↓
AI Summarizer (LLM via OpenRouter)
        ↓
Result Store (In-memory dictionary)
        ↓
UI displays result (via refresh)
```

---

## ⚙️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend Logic:** Python
* **AI Model:** OpenRouter (GPT-based models)
* **Architecture Pattern:** Producer–Consumer
* **Concurrency:** Multi-threading
* **Environment Management:** python-dotenv

---

## 🔥 Key Features

### ✅ Asynchronous Processing

* Tasks are queued and processed independently
* Eliminates blocking UI

### ✅ Producer–Consumer Model

* UI acts as **producer**
* Worker threads act as **consumers**

### ✅ Multi-Worker Scalability

* Multiple worker threads process tasks concurrently
* Easily scalable for higher load

### ✅ Request Tracking (UUID)

* Each request is assigned a unique ID
* Enables tracking of individual jobs

### ✅ Non-Blocking UI

* No `time.sleep()` blocking
* Uses refresh-based updates

### ✅ Error Handling

* Safe API calls with retry + timeout
* Displays meaningful error messages

---

## 📂 Project Structure

```
news-ai-summarizer/
│
├── app.py                # Streamlit UI (Producer)
├── worker.py             # Worker threads (Consumers)
│
├── src/
│   ├── queue_system.py   # Queue + result storage
│   ├── summarizer.py     # AI summarization logic
│
├── requirements.txt
├── .env (local only)
├── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/adv-async-news-ai-summarizer.git
cd adv-async-news-ai-summarizer
```

### 2️⃣ Create virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API key

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Deploy on Streamlit Cloud
3. Add secrets:

```toml
OPENROUTER_API_KEY = "your_api_key_here"
```

---

## 🧠 System Design Concepts Used

This project demonstrates key **Advanced System Design topics**:

* Asynchronous Processing
* Producer–Consumer Architecture
* Task Queues
* Multi-threading
* Decoupled Systems
* Scalable Worker Design

---

## ⚠️ Limitations

* In-memory queue (resets on restart)
* No persistent storage
* Limited by API rate limits

---

## 🚀 Future Improvements

* 🔹 Integrate Kafka / Redis (real message broker)
* 🔹 Add database (MongoDB / PostgreSQL)
* 🔹 Implement caching layer
* 🔹 Add request history UI
* 🔹 Add rate limiting & authentication
* 🔹 Convert worker to microservice (FastAPI)

---

## 💼 Use Case

* News aggregation platforms
* Content summarization tools
* AI-based information systems

---

## 🧑‍💻 Author

**Sahil Kelkar**

---

## 🎯 Project Type

Advanced System Design Mini Project
(B.Tech AIML)

---

## 🧠 How to Explain in Viva

> “I designed an asynchronous news summarization system using a producer-consumer architecture, where user requests are decoupled from processing using a task queue and handled by multiple worker threads for scalability.”

---

## ⭐ If you found this useful

Give this repo a star ⭐
