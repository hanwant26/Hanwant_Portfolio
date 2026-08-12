# Hanwant Singh — Personal Portfolio

A modern, responsive full-stack personal portfolio built with **Python and Flask** to showcase my skills, education, projects, resume, and contact information.

The application also includes a private admin dashboard for managing contact messages and uses **Neon PostgreSQL** for persistent production data storage.

---

## 🌐 Live Portfolio

### [View Live Portfolio](https://portfolio-hanwant.vercel.app)

```text
https://portfolio-hanwant.vercel.app
```

---

## 👨‍💻 About Me

I am a Computer Applications graduate currently pursuing a **Master of Computer Applications (MCA) in Data Science**.

My areas of interest include:

- Python Development
- Software Development
- Backend Development
- Web Development
- Data Science
- Database Systems

I enjoy building practical applications and continuously improving my programming, problem-solving, and software development skills.

---

# ✨ Portfolio Features

- Responsive modern dark interface
- Animated hero section
- Dynamic typing animation
- About section
- Technical skills section
- Featured projects
- Education section
- Resume viewer
- GitHub integration
- LinkedIn integration
- Contact form
- Scroll reveal animations
- Active navigation highlighting
- Mobile hamburger navigation
- Back-to-top button
- Custom favicon
- SEO metadata
- Social sharing metadata

---

# ⚙️ Backend Features

- Python Flask backend
- SQLite support for local development
- Neon PostgreSQL for production
- Contact message storage
- Server-side form validation
- Email format validation
- Environment-based configuration
- CSRF protection
- Request rate limiting
- Secure session configuration

---

# 🔐 Admin Dashboard

The portfolio includes a private administration panel for managing messages submitted through the contact form.

Features include:

- Secure admin authentication
- Hashed password verification
- Session-based authentication
- Contact message dashboard
- View contact submissions
- Reply through email
- Delete messages
- Secure POST-based logout
- CSRF-protected actions
- Login rate limiting

Admin routes are intentionally not linked from the public navigation.

---

# 🚀 Featured Project

## MeetVerse

**MeetVerse** is a real-time video conferencing platform built using Python and Django.

### Features

- Real-time video conferencing
- Room-based communication
- Persistent meeting chat
- Dynamic participant tracking
- Live meeting timer
- Secure room creation

### Technologies

`Python` `Django` `LiveKit` `SQLite` `JavaScript` `HTML5` `CSS3`

### Repository

https://github.com/hanwant26/MeetVerse

---

# 🛠️ Technical Skills

## Programming

- Python
- SQL
- JavaScript
- C++
- Shell Scripting

## Web Development

- Flask
- Django
- HTML5
- CSS3
- Bootstrap
- REST APIs

## Databases

- PostgreSQL
- MySQL
- SQLite
- SQL Queries
- Database Design

## Tools & Platforms

- Git
- GitHub
- Linux
- VS Code
- VirtualBox
- Vercel
- Neon

## Data Fundamentals

- Data Mining
- Data Warehousing
- Data Cleaning
- Data Visualization

## Computer Science Fundamentals

- Object-Oriented Programming
- DBMS
- Data Structures and Algorithms
- Software Engineering
- Operating Systems

---

# 🏗️ Production Architecture

```text
                     ┌─────────────────────┐
                     │       Visitor       │
                     └─────────┬───────────┘
                               │
                               ▼
                     ┌─────────────────────┐
                     │       Vercel        │
                     │                     │
                     │   Flask Portfolio   │
                     └─────────┬───────────┘
                               │
                         DATABASE_URL
                               │
                               ▼
                     ┌─────────────────────┐
                     │       Neon          │
                     │                     │
                     │    PostgreSQL       │
                     └─────────────────────┘
```

### Production

```text
Frontend + Flask Backend
        ↓
Vercel
        ↓
Neon PostgreSQL
```

### Local Development

```text
Flask
  ↓
SQLite
  ↓
portfolio.db
```

The application automatically uses PostgreSQL when `DATABASE_URL` is available and falls back to SQLite during local development.

---

# 📁 Project Structure

```text
Hanwant_Portfolio/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── 429.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── admin.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   ├── images/
│   │   ├── profile.jpg
│   │   └── favicon.svg
│   │
│   └── resume/
│       └── Hanwant_Singh_Resume.pdf
│
├── .env
├── .venv/
└── portfolio.db
```

The following are intentionally excluded from GitHub:

```text
.env
.venv/
portfolio.db
__pycache__/
.vscode/
```

---

# 💾 Database

The application supports two database modes.

## Local Development

SQLite is used when `DATABASE_URL` is not defined.

```text
portfolio.db
```

## Production

The deployed application uses:

```text
Neon PostgreSQL
```

through the environment variable:

```env
DATABASE_URL=postgresql://...
```

The database stores contact form submissions containing:

```text
Name
Email
Subject
Message
Created At
```

These messages can be viewed and managed through the private admin dashboard.

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/hanwant26/Hanwant_Portfolio.git
```

## 2. Enter the project directory

```bash
cd Hanwant_Portfolio
```

## 3. Create a virtual environment

Windows:

```bash
py -m venv .venv
```

## 4. Activate the virtual environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
SECRET_KEY=your-secret-key
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD_HASH=your-generated-password-hash

FLASK_DEBUG=1
SESSION_COOKIE_SECURE=0
```

For local SQLite development, `DATABASE_URL` can be omitted.

For PostgreSQL:

```env
DATABASE_URL=your-postgresql-connection-string
```

Never commit the `.env` file.

---

# 🔒 Generate Admin Password Hash

Generate a secure password hash:

```bash
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('YOUR_PASSWORD'))"
```

Store the generated value in:

```env
ADMIN_PASSWORD_HASH=your-generated-hash
```

The plaintext admin password is never stored in the source code.

---

# ▶️ Run Locally

Start the Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Admin login:

```text
http://127.0.0.1:5000/admin/login
```

---

# 🛡️ Security

The application currently includes:

- Hashed admin password authentication
- Environment variables for sensitive configuration
- CSRF protection
- POST-based admin logout
- CSRF-protected delete actions
- Server-side input validation
- Email format validation
- Input length limits
- Admin login rate limiting
- Contact form rate limiting
- HTTPOnly session cookies
- SameSite session protection
- Secure cookies in production
- Parameterized SQL queries
- Secrets excluded from Git
- Database records excluded from Git

---

# ☁️ Deployment

The production portfolio is deployed using:

### Application Hosting

**Vercel**

### Production Database

**Neon PostgreSQL**

### Source Control

**GitHub**

Production URL:

```text
https://portfolio-hanwant.vercel.app
```

Repository:

```text
https://github.com/hanwant26/Hanwant_Portfolio
```

---

# 🎓 Education

## Master of Computer Applications — Data Science

**Lovely Professional University**

2026 — Present

---

## Bachelor of Computer Applications — BCA (Science)

**Progressive Education Society's Modern College of Arts, Science and Commerce, Pune**

2022 — 2025

---

# 📬 Contact

## Hanwant Singh

### Portfolio

https://portfolio-hanwant.vercel.app

### GitHub

https://github.com/hanwant26

### LinkedIn

https://www.linkedin.com/in/hanwant-singh

### Email

singhhanwant325@gmail.com

---

# 📂 Repositories

### Portfolio

https://github.com/hanwant26/Hanwant_Portfolio

### MeetVerse

https://github.com/hanwant26/MeetVerse

---

# 📌 Project Status

**Live and actively maintained.**

Future updates will include additional projects and improvements as I continue expanding my software development and data science skills.

---

# 📄 License

This project is intended for personal portfolio and educational use.

© 2026 Hanwant Singh