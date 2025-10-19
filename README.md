🧠 Syncora X | YouTube → MP3 Converter
<div align="center"> <img src="https://img.shields.io/badge/Syncora%20X-Innovation%20In%20Code-4B9CD3?style=for-the-badge&logo=github" alt="Syncora X Badge" /> <h1>🧠 Syncora X | YouTube → MP3 Converter</h1> <p><strong>Full-Stack Learning Project for Syncora X Junior Members</strong></p> <p> <img src="https://img.shields.io/badge/React-Vite%20%2B%20Tailwind-blue?style=flat-square&logo=react" /> <img src="https://img.shields.io/badge/Django-REST%20%2B%20Celery%20%2B%20Redis-green?style=flat-square&logo=django" /> <img src="https://img.shields.io/badge/Deployment-Render%20%2F%20Vercel-black?style=flat-square&logo=vercel" /> </p> </div>
📘 Overview
This project is part of Syncora X's internal learning program for junior engineers.
It trains members to build and deploy production-grade full-stack systems with:

🧩 Asynchronous background processing

⚙️ Clean REST APIs

💅 Modern, reactive UI

# 🎯 Primary Objective
Build a YouTube → MP3 Converter that:

Accepts a YouTube URL

Converts it to MP3 via yt-dlp + ffmpeg

Lets users instantly download from browser

Stores download logs for analytics

# 🏗️ System Architecture
| **Component**                | **Technology / Tool**                              | **Description**                                                | **Responsibility**                                                 |
| ---------------------------- | -------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| 🎯 **Frontend (UI)**         | **React JS + Tailwind CSS**                        | Lightweight frontend interface integrated with React JS        | Displays YouTube input form, download status, and result           |
| ⚙️ **Backend Logic**         | **Python (Django)**                                 | Core logic layer handling requests and responses               | Processes YouTube URL, triggers audio download, and returns status |
| 🧠 **Downloader Engine**     | **yt-dlp**                                         | High-performance YouTube downloader library                    | Extracts metadata and downloads MP3/audio from YouTube videos      |
| 💾 **File Handling**         | **OS + Pathlib + Temporary Storage**               | Manages downloaded MP3 files and cleanup                       | Ensures proper file saving and cleanup after download              |
| ☁️ **Hosting (Backend)**     | **Render**                                         | Cloud platform for Flask-based Python apps                     | Hosts backend securely with automatic deploys from GitHub          |
| 🌐 **Frontend Deployment**   | **Vercel**                                         | High-performance static frontend hosting                       | Optional if UI is later separated into a React-based interface     |
| 🔒 **Version Control**       | **Git + GitHub (Syncora-X Org)**                   | Tracks source code changes and manages contributions           | Ensures teamwork, commit tracking, and pull request workflow       |
| 🧩 **Dependency Management** | **requirements.txt + pip**                         | Handles Python library installation                            | Keeps environment consistent across all developers                 |
| 🧑‍💻 **Team Workflow**      | **Syncora X Junior Members**                       | Guided by mentors and senior developers                        | Learn Flask, Python, Git, and deployment through real practice     |


# 🧠 Skill Targets
Backend (Celery + Redis + Django REST)

Frontend (Vite + Tailwind + Axios)

Full-stack integration

Deployment workflows (Render + Vercel)

Git branching & collaboration

# ⚙️ Setup & Run Locally

## 🪄 Step-by-Step Setup

#### 1️⃣ Clone & Install
```bash
git clone https://github.com/Syncora-X/youtube-mp3-converter.git
cd youtube-mp3-converter/backend
python -m venv venv
```

### Activate venv

#### Windows:
```bash
.\venv\Scripts\activate
```
#### macOS/Linux:
source venv/bin/activate
```bash
pip install -r requirements.txt
```

### 2️⃣ Environment Variables
Create .env inside /backend:

env
```bash
SECRET_KEY=syncora-x-secret
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://127.0.0.1:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 3️⃣ Run Redis
```bash
docker run -d -p 6379:6379 redis
```

## 4️⃣ Start Celery & Django

#### Terminal 1 - Celery Worker
```bash
celery -A youtube_mp3_backend.celery worker --loglevel=info --pool=solo
```

#### Terminal 2 - Django Server
```bash
python manage.py migrate
python manage.py runserver
```

## 5️⃣ Run Frontend
```bash
cd ../frontend
npm install
VITE_API_URL=http://127.0.0.1:8000/api npm run dev
```

### 🚀 Deployment Guide

🖥️ Backend → Render
Connect GitHub repo → New Web Service

Build Command:

```bash
pip install -r requirements.txt
```
Start Command:

```bash
gunicorn youtube_mp3_backend.wsgi:application
```
Add Environment Variables:

SECRET_KEY

REDIS_URL

DATABASE_URL

ALLOWED_HOSTS

Create Background Worker:

```bash
celery -A youtube_mp3_backend.celery worker --loglevel=info
```
## 🌐 Frontend → Vercel
Select /frontend directory

Build Command: npm run build

Output Directory: dist

Add Environment Variable:

env
```bash
VITE_API_URL=https://your-backend.onrender.com/api
```

## ⚡ Environment Variables Reference
| Variable        | Description           | Example                         |
| --------------- | --------------------- | ------------------------------- |
| `SECRET_KEY`    | Django secret key     | `syncora-x-secret`              |
| `DEBUG`         | Development mode flag | `True`                          |
| `DATABASE_URL`  | DB connection         | `sqlite:///db.sqlite3`          |
| `REDIS_URL`     | Celery broker URL     | `redis://localhost:6379/0`      |
| `ALLOWED_HOSTS` | Allowed domains       | `localhost,127.0.0.1`           |
| `VITE_API_URL`  | API endpoint          | `https://api.syncora-x.com/api` |

## 💾 File Download Mechanism
🎵 After Celery finishes, MP3 is saved in media/downloads/

📁 API endpoint /api/download/<id>/file/ sends file with Content-Disposition: attachment

➡️ Browser triggers Chrome-style download popup

## 🧩 Future Development Roadmap
| Phase      | Focus     | Features                              |
| ---------- | --------- | ------------------------------------- |
| 🧱 Phase 2 | UI & UX   | Download progress, history, dark mode |
| ⚙️ Phase 3 | Backend   | JWT auth, S3 storage, WebSockets      |
| 📊 Phase 4 | Analytics | Charts, dashboards, task tracking     |

### 📊 Phase 4	Analytics	Charts, stats, dashboard for metrics
## 🧠 Learning Outcomes
| Area     | Skill Developed                                   |
| -------- | ------------------------------------------------- |
| Backend  | Django REST + Celery async tasks                  |
| Frontend | React (Vite + Tailwind) + API integration         |
| DevOps   | Render & Vercel deployment                        |
| Team     | GitHub workflow, PRs, reviews                     |
| Product  | Architecture to deployment pipeline understanding |

## 🛡️ Legal & Ethical Note
⚠️ This project is for educational purposes only under the Syncora X internal training program.
Members must respect YouTube Terms of Service and copyright laws.
Do not distribute or use this tool for unauthorized downloads.

## 🤝 Contributing (Syncora X Members)
Fork this repository

Create a new branch: feature/<yourname>

Commit descriptive messages

Open a Pull Request for mentor review

Merge after approval

# 🧭 Roadmap Summary
| Quarter | Milestone                        |
| ------- | -------------------------------- |
| Q4 2025 | 🎨 UI Upgrade + Download History |
| Q1 2026 | 🔐 Auth + S3 Integration         |
| Q2 2026 | 📊 Dashboard + Analytics         |
| Q3 2026 | 📱 Mobile-First PWA Version      |

# 🪄 Maintainers
# Syncora X Engineering Team

 👨‍💻 Lead Mentor: Ashan Mir

👩‍💻 Junior Developers: Batch 2025 – Full Stack Interns

📧 Contact: support@syncora-x.com

🌐 Website: https://syncora-x.com

# 📜 License
© 2025 Syncora X. All Rights Reserved.
Licensed under the Syncora X Open Training License — for educational and internal demonstration only.

<div align="center"> <sub>Built with ❤️ by the Syncora X Learning Community</sub> </div>
