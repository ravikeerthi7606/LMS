# EduFlow LMS

A full-featured Learning Management System built with **FastAPI**, **React**, and **MongoDB**.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI + Motor (async MongoDB) |
| Frontend | React 18 + Vite + TailwindCSS |
| Database | MongoDB (local via Compass or Atlas for cloud) |
| Video Storage | Firebase Storage (signed URLs) |
| Payments | Razorpay / Stripe |
| Real-time | WebSockets (Socket.IO) |
| Auth | JWT (access + refresh tokens) + OTP email verification |

---

## Features

### Student
- Register/Login with OTP email verification, Google/GitHub social login
- Browse, search, and filter courses with autocomplete
- Enroll with promo codes and payment gateway
- Secure video streaming (signed Firebase URLs, non-downloadable player)
- Raise doubts (public/private tickets), receive notifications when resolved
- Take tests/assignments, view results and leaderboard
- Track watch hours and course progress
- Follow teachers, receive content notifications
- Download certificates (PDF) on course completion
- Dedicated progress dashboard with charts

### Teacher
- Upload courses with metadata, tags, thumbnail
- Upload videos via Firebase Storage (chunked, progress bar)
- Upload course materials (PDFs, docs)
- Manage student doubts with ticket tracking (open → in_progress → resolved)
- Create tests with MCQ, short-answer, true/false questions
- Schedule and host live sessions
- View per-course analytics (views, students, revenue)
- Earnings dashboard with transaction history and payout tracking
- Customizable certificate templates
- Offer/promo code suggestions based on trending topics

### Admin
- User management (activate/deactivate/delete)
- Platform revenue dashboard
- Content moderation
- Promo code management
- Payout processing

---

## Project Structure

```
lms/
├── backend/
│   ├── main.py                 # FastAPI app + middleware + routing
│   ├── config.py               # Settings (pydantic-settings)
│   ├── database.py             # MongoDB connection + indexes
│   ├── schemas/schemas.py      # All Pydantic models
│   ├── routes/
│   │   ├── auth.py             # Register, login, OTP, social, refresh
│   │   ├── courses.py          # CRUD, search, trending, recommendations
│   │   ├── videos.py           # Firebase upload, stream URL, progress
│   │   ├── doubts.py           # Ticket system with replies and status
│   │   ├── tests.py            # Create tests, submit, grade, leaderboard
│   │   ├── payments.py         # Razorpay/Stripe initiate + verify
│   │   ├── users.py            # Profile, notifications, reviews, follows, certs, live
│   │   └── websocket_admin.py  # WebSocket for real-time + admin panel
│   ├── middleware/
│   │   └── dependencies.py     # JWT auth dependency
│   └── utils/
│       ├── auth_utils.py       # JWT, bcrypt, OTP
│       ├── email_utils.py      # SMTP email sender
│       ├── firebase_utils.py   # Firebase admin + signed URLs
│       └── certificate_utils.py# PDF certificate generation
│
└── frontend/
    ├── src/
    │   ├── App.jsx             # Routes (public, student, teacher, admin)
    │   ├── context/AuthContext.jsx   # Auth state + login/logout
    │   ├── utils/api.js        # Axios client + all API calls
    │   ├── components/
    │   │   ├── layout/Layout.jsx     # Nav + notification bell
    │   │   ├── layout/AuthLayout.jsx
    │   │   └── common/CourseCard.jsx
    │   └── pages/
    │       ├── Home.jsx              # Hero, trending, recommendations
    │       ├── CourseDetail.jsx      # Course page + enrollment + payment
    │       ├── SearchResults.jsx     # Full-text search + filters
    │       ├── TeacherProfile.jsx    # Public teacher page + follow
    │       ├── auth/                 # Login, Register, OTP, ForgotPassword
    │       ├── student/              # Dashboard, VideoPlayer, Doubts, Progress, Certs, Tests
    │       ├── teacher/              # Dashboard, Courses, Upload, Doubts, Tests, Earnings, Live
    │       └── admin/                # Dashboard, Users
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB Compass (local) or MongoDB Atlas (cloud)
- Firebase project (for video storage)

### 1. Backend Setup

```bash
cd backend
cp .env.example .env
# Edit .env with your credentials

pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

### 2. Frontend Setup

```bash
cd frontend
cp .env.example .env
# Edit .env with your Firebase and API keys

npm install
npm run dev
```

App: http://localhost:5173

### 3. MongoDB Compass
- Connect to `mongodb://localhost:27017`
- Database `lms_db` is auto-created on first run
- Indexes are created automatically on startup

---

## Scaling to Cloud

### MongoDB → Atlas
```
MONGODB_URL=mongodb+srv://<user>:<pass>@cluster.xxxxx.mongodb.net/lms_db
```

### Video Storage → Firebase
1. Create Firebase project
2. Enable Firebase Storage
3. Download service account JSON → set `FIREBASE_CREDENTIALS_PATH`
4. Set `FIREBASE_STORAGE_BUCKET`

### Deployment
- **Backend**: Deploy to Railway, Render, or EC2 (Dockerfile provided)
- **Frontend**: Deploy to Vercel (`npm run build`)
- **WebSockets**: Ensure sticky sessions or use Redis adapter

---

## API Endpoints Summary

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/auth/register` | Register user |
| POST | `/api/v1/auth/login` | Login |
| POST | `/api/v1/auth/verify-otp` | Verify email OTP |
| GET | `/api/v1/courses/search` | Search courses |
| GET | `/api/v1/courses/trending` | Trending courses |
| POST | `/api/v1/videos/upload-url` | Get Firebase upload URL |
| GET | `/api/v1/videos/{id}/stream-url` | Get signed stream URL |
| POST | `/api/v1/doubts` | Create doubt ticket |
| POST | `/api/v1/doubts/{id}/reply` | Reply to doubt |
| POST | `/api/v1/tests/{id}/submit` | Submit test |
| POST | `/api/v1/payments/initiate` | Start payment |
| GET | `/api/v1/certificates/course/{id}` | Download certificate PDF |
| WS | `/ws/{user_id}` | Real-time notifications |

Full interactive docs at `/docs` (Swagger UI).