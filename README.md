YouTube → MP3 Converter

Full-stack starter (Django REST + Celery + yt-dlp + React(Vite) + Tailwind)

A complete from-scratch project that lets users paste a YouTube link, converts the video to MP3 on the server, stores the MP3, and provides a download link. This README explains project architecture, local development, production deploy (Render for backend, Vercel for frontend), environment variables, troubleshooting, and extra production notes.

Table of contents

Project overview & architecture

What’s included

Quick local setup (dev)

How the API works (endpoints & flow)

Production deployment overview

Deploy backend to Render (recommended)

Deploy frontend to Vercel

Environment variables

Media storage & serving options

Security & legal considerations

Troubleshooting & common errors

Next improvements / roadmap

License

Project overview & architecture
Client (React + Vite/Tailwind)
  ↕ axios
Backend (Django + DRF)
  ↳ REST endpoints
  ↳ Celery tasks (yt-dlp + ffmpeg) -----> Redis (broker)
  ↳ Saves MP3 files to /media/downloads or S3
Database (Postgres) - stores users + download history


Flow when user requests a conversion:

User pastes YouTube URL in React UI and clicks Convert.

Frontend POSTs to Django API /api/download/.

Django creates a Download DB entry (optional) and enqueues a Celery task.

Celery worker runs yt-dlp + ffmpeg to download & convert. File saved to media/downloads/ (or S3).

Frontend polls or is notified; when ready user requests /api/downloads/<id>/file/ to stream/force-download the MP3.

What’s included

Backend: Django + Django REST Framework

Async Worker: Celery (Redis broker)

Downloader: yt-dlp + ffmpeg (local conversion)

Frontend: React (Vite) + TailwindCSS — minimal UI for URL input and history

Dockerfile & docker-compose (starter) — optional

Example requirements.txt and .gitignore included in repo

Quick local setup (dev)

These are the steps to run everything locally on Windows / macOS / Linux. Use PowerShell / terminal.

Prereqs

Python 3.10+

Node 18+ and npm

ffmpeg installed on your machine (or included in Docker)

Redis (local) or Docker (recommended)

yt-dlp (installed into Python venv via requirements)

1) Clone & venv
git clone https://github.com/<your-user>/youtube-mp3-converter.git
cd youtube-mp3-converter/backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt

2) Configure env

Create backend/.env or set env vars. Minimum for local dev (SQLite + Redis on localhost):

SECRET_KEY=dev-secret
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://127.0.0.1:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1


If you prefer sqlite, use DATABASES setup in settings.py as provided.

3) Start Redis

On macOS/Linux if installed:

redis-server


Or with Docker:

docker run -d -p 6379:6379 redis

4) Run migrations & create superuser
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5) Start Celery worker (Windows note)

Windows: use --pool=solo to avoid multiprocessing issues:

celery -A youtube_mp3_backend.celery worker --loglevel=info --pool=solo


Linux/macOS:

celery -A youtube_mp3_backend.celery worker --loglevel=info

6) Run Django server
python manage.py runserver

7) Start frontend
cd ../frontend
npm install
# dev server (Vite)
VITE_API_URL=http://127.0.0.1:8000/api npm run dev


Frontend default: http://localhost:5173
Backend default: http://127.0.0.1:8000

How the API works (endpoints & flow)

Example endpoints from the starter:

POST /api/download/

Body: { "url": "<youtube_url>" }

Response: { status: "Download started", task_id: "<celery-task-id>", url: "<original>" }

This enqueues a Celery job that downloads & converts to MP3 in background.

GET /api/downloads/

List user’s downloads (history).

GET /api/downloads/<id>/file/

If task completed, returns FileResponse with Content-Disposition: attachment to force Chrome download.

Note: For production you should protect endpoints (authentication) and implement rate limits.

Production deployment overview
Deploy backend to Render (recommended)

You can deploy the Django app as a Docker service or as a Python service. I recommend Docker (we included a Dockerfile in /backend).

Steps summary (Render dashboard):

Create a new Web Service on Render → connect your GitHub repo.

Use either:

Docker: Render will build your Dockerfile; or

Python service: set Build command pip install -r requirements.txt and Start command gunicorn youtube_mp3_backend.wsgi:application.

Add environment variables in Render dashboard:

SECRET_KEY, DEBUG=False, DATABASE_URL (managed Postgres), REDIS_URL (managed Redis), ALLOWED_HOSTS.

Add a Background Worker (Render service) to run Celery:

Command: celery -A youtube_mp3_backend.celery worker --loglevel=info

Ensure Redis URL and any S3 credentials are set for this worker.

For media files in production, use S3 or DigitalOcean Spaces (see Media section) — don’t rely on filesystem for multiple dynos.

Notes for Render:

Use managed Postgres/Redis from Render (or external providers).

Ensure you expose /media/ if serving files directly (or use signed S3 URLs).

Deploy frontend to Vercel

Create a new Vercel project, connect GitHub repo, select frontend directory.

Set Build command: npm run build (Vite).

Set Output directory: dist (Vite default).

In Vercel environment variables, add:

VITE_API_URL=https://YOUR_BACKEND_URL/api (point to Render backend)

Deploy. Vercel will serve static front-end; client will call your backend API.

Environment variables
Name	Purpose	Example
SECRET_KEY	Django secret	a-very-secret-key
DEBUG	Debug mode	False
DATABASE_URL	Database connection	postgres://user:pass@host:5432/dbname
REDIS_URL	Celery broker/result backend	redis://:password@host:6379/0
ALLOWED_HOSTS	Comma separated hosts	example.com,api.example.com
VITE_API_URL	Frontend → API URL (Vercel)	https://api.example.com/api
AWS_S3_BUCKET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION	Optional for S3 storage	—
Media storage & serving options

Local (dev)

Save files under backend/downloads/ or backend/media/downloads/. Works for single-instance dev, not for multiple servers.

S3 / DigitalOcean Spaces (production)

Save files to S3. On job completion create a signed URL (expires) or store public object and return link.

Use django-storages[boto3] and set DEFAULT_FILE_STORAGE to storages.backends.s3boto3.S3Boto3Storage.

Why S3 in production?

Multiple backend instances, horizontal scaling, persistence beyond ephemeral filesystem, better CDN/edge delivery.

Security & legal considerations

Rate limiting & authentication: Protect the API with user auth (JWT/session) and rate limit conversions per user/IP to prevent abuse.

YouTube Terms of Service: Downloading content from YouTube may violate YouTube’s ToS or copyright law for certain materials. Use this tool responsibly; restrict or disallow copyrighted content or require that users only download content they own or have rights to.

Resource costs: Converting many files uses CPU and disk; consider job queue limits, file size limits, and user quotas.

Sanitize filenames & validate URLs to avoid directory traversal or injection issues.

Troubleshooting & common errors

CORS blocked by browser

Install django-cors-headers and add to INSTALLED_APPS and MIDDLEWARE, then set CORS_ALLOWED_ORIGINS = ["https://your-frontend"] (or CORS_ALLOW_ALL_ORIGINS = True for dev).

Celery worker failing on Windows

Use --pool=solo on Windows:
celery -A youtube_mp3_backend.celery worker --loglevel=info --pool=solo

Or run Celery inside WSL2 / Docker / Linux server for production.

psycopg2 errors

Install psycopg2-binary in venv for Postgres or switch to SQLite for quick dev.

yt-dlp downloading playlists instead of single video

Add noplaylist=True to ydl_opts (or --no-playlist) if you want single-video behavior.

Not seeing download in Chrome

Server-side download saves file on server. To trigger browser download, serve the file via an endpoint with Content-Disposition: attachment and make frontend navigate to that URL or use <a download>.

Permissions / file handles errors on Windows

Run terminals as Administrator if you hit permission issues. Use Docker/WSL if you keep encountering handle/Semaphores errors.

Next improvements / roadmap

Add JWT auth & account management (signup/login)

User download quotas and rate limiting

Real-time progress updates via WebSockets / Server-Sent Events (SSE)

S3-backed media storage + signed download URLs

Job cancellation and retry support

Better UI: queue status, progress bars, thumbnails

Useful commands / quick cheatsheet

Migrate & run dev:

cd backend
source venv/bin/activate             # or .\venv\Scripts\activate (Windows)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Start celery:

# Linux/macOS
celery -A youtube_mp3_backend.celery worker --loglevel=info
# Windows (use solo pool)
celery -A youtube_mp3_backend.celery worker --loglevel=info --pool=solo


Build & serve frontend:

cd frontend
npm install
npm run build
# Vite preview (production-ish)
npm run preview


Docker (if you use docker-compose):

docker-compose up --build

README badges & showcase (optional)

Add CI badges, license, or demo link here (if deployed).

License

MIT — include license file if you want to publish as open source.
