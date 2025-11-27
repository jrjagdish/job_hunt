🧩 JobHunt AI Extension — Backend + Chrome Extension + React UI

A smart job-assistant tool that extracts job details from sites like LinkedIn/Indeed and helps users track applications, detect ghosting, and improve job-search efficiency.

🚀 Project Overview

JobHunt AI is a 3-part system:

1️⃣ Chrome Extension (Local Installation — No Store Needed)

Extract job data from LinkedIn, Naukri, Indeed, etc.

Send job details to backend API

Provide keywords, skill match %, and quick-apply shortcuts

2️⃣ Django REST Backend

Auth (JWT)

Job tracking (applied, interviewing, ghosted, rejected)

Redis caching

Rate limiting

User analytics (how many applied, which platform, success rate)

3️⃣ React Frontend

Dashboard for job tracking

Download Chrome extension (.zip)

View job insights

Settings, API Key generation

🏗 Tech Stack
Backend

Python

Django

Django REST Framework

PostgreSQL / SQLite

Redis

JWT Authentication

Docker (optional)

Frontend

React + Vite

Tailwind CSS

Extension

Manifest V3

Content scripts

Background service worker

Messaging API



Create .env in backend root:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379
JWT_ACCESS_TOKEN_LIFETIME=30

⚙️ Installation & Setup
Backend Setup
git clone https://github.com/your-username/jobhunt-backend.git
cd jobhunt-backend

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

🧪 API Endpoints Overview
Auth
Method	Endpoint	Description
POST	/api/auth/register/	Create user
POST	/api/auth/login/	Login, get tokens
GET	/api/auth/me/	Get profile
Jobs
Method	Endpoint	Description
POST	/api/jobs/submit/	Used by extension to send job info
GET	/api/jobs/	List jobs
PATCH	/api/jobs/<id>/status/	Update status
GET	/api/jobs/stats/	Analytics
📦 Chrome Extension Installation

(Since you avoid Chrome Web Store fees)

Steps:

Download jobhunt-extension.zip from your frontend site

Extract it

Go to: chrome://extensions/

Enable Developer Mode

Click Load Unpacked

Select folder

Done 🎉

🔥 Features Roadmap
Week 1 – Backend

✔ User Model
✔ Auth (JWT)
✔ Jobs Model
✔ Submit endpoint for extension
✔ Redis caching
✔ Rate limiting
✔ Status tracking

Week 2 – Frontend + Extension

✔ React UI basic
✔ Extension popup UI
✔ Extension → Backend API
✔ Download ZIP button
✔ Job dashboard
✔ Analytics charts

Future

AI-based job score

Job spam detection

Ghost detection

Auto-track application progress

Resume recommendation

🎯 Learning Outcomes

You will learn:

Real-world Django + DRF project structure

JWT authentication

Chrome extension development

API + browser communication

Redis rate limiting + caching

React frontend integration

Product thinking (MVP → Scalable)

Deployment with Docker

Full-stack architecture

