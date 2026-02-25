# 🎓 LMS Web Application

A full-stack Learning Management System (LMS) built using:

- 🔹 Frontend: React (Vite)
- 🔹 Backend: Flask (REST API)
- 🔹 Database: MongoDB
- 🔹 Authentication: JWT (JSON Web Token)
- 🔹 Password Security: Bcrypt

---

## 📌 Project Overview

This LMS application provides:

✔ User Registration (Student / Teacher)  
✔ Secure Login Authentication  
✔ JWT Token-Based Authorization  
✔ Protected Routes  
✔ MongoDB Database Integration  
✔ CORS Enabled for Frontend-Backend Communication  

---

## 🏗️ Project Architecture

```
React (Frontend)
      ↓
Axios API Calls
      ↓
Flask REST API
      ↓
MongoDB Database
```

---

# ⚙️ Backend Setup (Flask API)

## 📁 Backend Structure

```
backend/
│── app.py
│── config.py
│── .env
│── requirements.txt
```

## 🔧 Installation Steps

### 1️⃣ Create Virtual Environment
```
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

If requirements.txt not created:
```
pip install flask flask-pymongo flask-bcrypt flask-jwt-extended flask-cors python-dotenv
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file:

```
MONGO_URI=your_mongodb_connection_string
JWT_SECRET_KEY=your_secret_key
```

---

## ▶️ Run Backend Server

```
python app.py
```

Server runs on:
```
http://127.0.0.1:5000
```

---

# 🌐 API Endpoints

## 🔹 Register
POST `/api/register`

Request Body:
```
{
  "name": "Ravi",
  "email": "ravi@gmail.com",
  "password": "123456",
  "role": "student"
}
```

Response:
```
User registered successfully
```

---

## 🔹 Login
POST `/api/login`

Request Body:
```
{
  "email": "ravi@gmail.com",
  "password": "123456"
}
```

Response:
```
{
  "access_token": "JWT_TOKEN"
}
```

---

## 🔹 Protected Route
GET `/api/profile`

Header:
```
Authorization: Bearer JWT_TOKEN
```

Response:
```
Welcome user_email
```

---

# 💻 Frontend Setup (React + Vite)

## 📁 Frontend Structure

```
frontend/
│── src/
│    ├── Login.jsx
│    ├── Register.jsx
│    ├── authService.js
│── package.json
```

---

## 🔧 Install Dependencies

```
npm install
```

---

## ▶️ Run Frontend

```
npm run dev
```

Frontend runs on:
```
http://localhost:5173
```

---

# 🔐 Authentication Flow

1️⃣ User registers → Password hashed using Bcrypt  
2️⃣ User logs in → Backend verifies credentials  
3️⃣ JWT token generated  
4️⃣ Frontend stores token  
5️⃣ Protected routes validate token  

---

# 🔒 Security Features

- Password hashing (Bcrypt)
- JWT Token authentication
- CORS enabled
- Environment-based configuration
- Secure MongoDB connection

---

# 🚀 Future Improvements

- Role-based dashboard (Student / Teacher)
- Course creation module
- Video streaming integration
- Payment gateway
- Admin control panel
- Forgot password / Reset password
- Email verification
- Production deployment (AWS / Render / Railway)

---

# 📊 Tech Stack Summary

| Layer        | Technology |
|-------------|------------|
| Frontend    | React + Vite |
| Backend     | Flask |
| Database    | MongoDB |
| Auth        | JWT |
| Security    | Bcrypt |
| API Client  | Axios |

---

# 👨‍💻 Developer Notes

- Debug mode enabled (for development only)
- Do NOT use debug=True in production
- Always store JWT secret securely
- Use HTTPS in production
- Use proper MongoDB Atlas IP whitelist

---

# 📜 License

This project is for educational and R&D purposes.

---

# ✨ Author

Ravi  
IT – R&D Project (LMS Development)

---

# 🎯 Status

✔ Authentication Completed  
✔ Backend API Working  
✔ Frontend Login & Register Working  
🚧 Home Page Under Development  
🚧 Course Module Pending  

---