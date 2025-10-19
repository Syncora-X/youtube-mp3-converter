🧠 Syncora X | YouTube → MP3 Converter

Full-Stack Learning Project for Syncora X Junior Members
React (Vite + Tailwind) × Django REST + Celery × yt-dlp × Redis × Render / Vercel Deployment

📘 Overview

This project is part of Syncora X’s internal learning program for junior engineers.
The goal is to teach our members how to build, structure, and deploy production-grade full-stack systems with asynchronous background processing, clean REST APIs, and modern front-end architecture.

🧩 Primary Objective
Build a real-world YouTube-to-MP3 converter web app that:

Accepts a YouTube URL

Converts it to MP3 on the server using yt-dlp + ffmpeg

Lets users download the file directly via browser

Stores download logs for future analytics

 ┌───────────────────────┐
 │   React (Vite) UI     │  →  Handles user input & progress
 │   Tailwind + Axios    │
 └──────────┬────────────┘
            │ REST API
 ┌──────────▼────────────┐
 │ Django + DRF Backend  │  →  Validates request, queues Celery task
 │ Celery Worker + Redis │  →  Runs yt-dlp + ffmpeg in background
 └──────────┬────────────┘
            │
        Stores output
            │
     ┌──────▼──────┐
     │ Media / S3  │  →  Serves MP3 file via secure link
     └─────────────┘

🧑‍💻 How Junior Members Work on It
🔹 Team Workflow

| Stage             | Responsibility                                           | Tools                        |
| ----------------- | -------------------------------------------------------- | ---------------------------- |
| 1. Clone & Setup  | Each member forks the repo and sets up local environment | Git + Virtual Env            |
| 2. Feature Branch | Work on individual module (API, UI, Celery worker, etc.) | Branching (`feature/<name>`) |
| 3. Review         | Senior review via Pull Request                           | GitHub PR + Code Review      |
| 4. Merge          | Only after approval                                      | Protected main branch        |
| 5. Deploy         | Backend → Render, Frontend → Vercel                      | DevOps training              |


🔹 Skill Targets

Backend (API design, Celery async tasks, Redis integration)

Frontend (Vite + Tailwind + Axios calls + state handling)

Full-stack integration (CORS, async file downloads)

Cloud deployment (Render / Vercel)

GitHub workflow & version control best practices

⚙️ Setup & Run Locally
1️⃣ Clone & Install
git clone https://github.com/Syncora-X/youtube-mp3-converter.git
cd youtube-mp3-converter/backend
python -m venv venv
# Activate venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt

2️⃣ Environment Variables

Create .env in backend/:

SECRET_KEY=syncora-x-secret
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://127.0.0.1:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1

3️⃣ Run Redis
docker run -d -p 6379:6379 redis

4️⃣ Start Celery & Server
celery -A youtube_mp3_backend.celery worker --loglevel=info --pool=solo  # Windows
python manage.py runserver

5️⃣ Frontend
cd ../frontend
npm install
VITE_API_URL=http://127.0.0.1:8000/api npm run dev

🚀 Deployment Guide
🖥️ Backend → Render

Connect GitHub repo → New Web Service

Build Command: pip install -r requirements.txt

Start Command: gunicorn youtube_mp3_backend.wsgi:application

Add env vars (SECRET_KEY, REDIS_URL, DB URL, ALLOWED_HOSTS)

Create Background Worker for Celery:

celery -A youtube_mp3_backend.celery worker --loglevel=info

🌐 Frontend → Vercel

Connect repo → select /frontend directory

Build: npm run build

Output Dir: dist

Environment:

VITE_API_URL=https://your-backend.onrender.com/api


| Variable      | Description             | Example                                                        |
| ------------- | ----------------------- | -------------------------------------------------------------- |
| SECRET_KEY    | Django secret key       | syncora-x-secret                                               |
| DEBUG         | Dev mode flag           | False                                                          |
| DATABASE_URL  | DB connection           | postgres://user:pass@host/db                                   |
| REDIS_URL     | Celery broker           | redis://:password@host:6379/0                                  |
| ALLOWED_HOSTS | Comma separated domains | youtube.syncora-x.com                                          |
| VITE_API_URL  | Frontend API URL        | [https://api.syncora-x.com/api](https://api.syncora-x.com/api) |

💾 File Download Mechanism

File saved in media/downloads/ after Celery finishes.

/api/download/<id>/file/ returns Content-Disposition: attachment, so browser forces Chrome download (like a normal website).

🧩 Planned Future Work (For Junior Members)
🎯 Phase 2 – Improved UI and UX

Modern download progress visualization

Persistent download history with date, title, and size

Audio preview & metadata display

Themed Syncora X branding UI (gradient, logo, dark mode)

🎯 Phase 3 – Backend Enhancements

User authentication (JWT)

Rate limiting per IP or account

S3 storage + signed download URLs

Progress notifications via WebSocket/SSE

Job retry logic and error tracking (Sentry)

🎯 Phase 4 – Analytics and Insights

Store download logs in DB

Display charts (React + Recharts or Chart.js)

Dashboard for usage metrics and Celery task stats
| Area             | Skill Developed                                    |
| ---------------- | -------------------------------------------------- |
| Backend          | Django REST API design + Celery async processing   |
| Frontend         | React (Vite + Tailwind), API integration           |
| DevOps           | Render / Vercel CI pipeline setup                  |
| Team             | GitHub branching, PR workflow, review discipline   |
| Product Thinking | Designing features from architecture to deployment |

🛡️ Legal & Ethical Note

This project is purely for educational & internal training at Syncora X.
All members must comply with YouTube Terms of Service and local copyright laws.
Do not distribute or use this for downloading copyrighted media.

🤝 Contributing Guidelines (for Syncora X Team)

Fork → Branch (feature/<yourname>)

Commit descriptive messages

Push & open a Pull Request

Request review from mentors

Merge only after approval

🧭 Roadmap Summary
Quarter	Milestone
Q4 2025	UI upgrade + Download history
Q1 2026	Auth + S3 integration
Q2 2026	Dashboard + Analytics
Q3 2026	Mobile-first PWA interface
🪄 Maintainers

Syncora X Engineering Team
Lead Mentor: Ashan Mir
Junior Developers: Batch 2025 – Full Stack Interns

📧 Contact → support@syncora-x.com

🌐 Website → https://syncora-x.com

📜 License

© 2025 Syncora X. All Rights Reserved.
This repository is for internal learning and demonstration under the Syncora X Open Training License (educational use only).
