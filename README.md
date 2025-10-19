<div align="center">
  <img src="https://img.shields.io/badge/Syncora%20X-Innovation%20In%20Code-4B9CD3?style=for-the-badge&logo=github" alt="Syncora X Badge" />
  <h1>🧠 Syncora X | YouTube → MP3 Converter</h1>
  <p><strong>Full-Stack Learning Project for Syncora X Junior Members</strong></p>
  <p>
    <img src="https://img.shields.io/badge/React-Vite%20%2B%20Tailwind-blue?style=flat-square&logo=react" />
    <img src="https://img.shields.io/badge/Django-REST%20%2B%20Celery%20%2B%20Redis-green?style=flat-square&logo=django" />
    <img src="https://img.shields.io/badge/Deployment-Render%20%2F%20Vercel-black?style=flat-square&logo=vercel" />
  </p>
</div>

---

## 📘 Overview

This project is part of **Syncora X’s internal learning program** for junior engineers.  
It trains members to build and deploy **production-grade full-stack systems** with:

- 🧩 Asynchronous background processing  
- ⚙️ Clean REST APIs  
- 💅 Modern, reactive front-end architecture  

---

## 🎯 Primary Objective

Build a **YouTube → MP3 Converter** that:
- Accepts a YouTube URL  
- Converts it to MP3 using `yt-dlp` + `ffmpeg`  
- Lets users instantly download from the browser  
- Stores download logs for analytics  

---

## 🏗️ System Architecture

┌────────────────────────┐
│ 🎨 React (Vite) UI │ → Handles user input & progress
│ ⚡ Tailwind + Axios │
└──────────┬──────────────┘
│ REST API
┌──────────▼──────────────┐
│ 🧠 Django + DRF Backend │ → Validates & queues Celery task
│ ⚙️ Celery Worker + Redis │ → Runs yt-dlp + ffmpeg in background
└──────────┬──────────────┘
│
Stores Output
│
┌──────▼──────┐
│ 💾 Media/S3 │ → Serves MP3 file via secure link
└─────────────┘

---

## 👩‍💻 How Junior Members Work on It

### 🧭 Team Workflow

| Stage | Responsibility | Tools |
|-------|----------------|-------|
| 🧩 1. Clone & Setup | Fork repo & set up local environment | Git + venv |
| 🌿 2. Feature Branch | Work on individual module | `feature/<name>` |
| 🔍 3. Review | Senior review via Pull Request | GitHub PR |
| 🔒 4. Merge | Only after approval | Protected main branch |
| 🚀 5. Deploy | Backend → Render, Frontend → Vercel | DevOps |

---

### 🧠 Skill Targets
- Backend: Django REST, Celery, Redis  
- Frontend: React (Vite), Tailwind, Axios  
- Full-stack Integration & API communication  
- Deployment (Render + Vercel)  
- Git branching, PRs & collaboration  

---

## ⚙️ Setup & Run Locally

<details>
<summary>🪄 <b>Step-by-Step Setup</b></summary>

### 1️⃣ Clone & Install
```bash
git clone https://github.com/Syncora-X/youtube-mp3-converter.git
cd youtube-mp3-converter/backend
python -m venv venv

Activate the virtual environment:
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Then install dependencies:
pip install -r requirements.txt

### 2️⃣ Create Environment Variables
```bash
Create a .env file inside /backend:

SECRET_KEY=syncora-x-secret
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://127.0.0.1:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1


### 3️⃣ Run Redis
```bash
docker run -d -p 6379:6379 redis

### 4️⃣ Start Celery & Django Server
```bash
celery -A youtube_mp3_backend.celery worker --loglevel=info --pool=solo
python manage.py runserver

### 5️⃣ Run Frontend
```bash
cd ../frontend
npm install
VITE_API_URL=http://127.0.0.1:8000/api npm run dev

</details>
