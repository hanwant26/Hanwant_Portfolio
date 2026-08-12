# Hanwant Singh — Personal Portfolio

A modern and responsive personal portfolio website built with **Python and Flask** to showcase my skills, education, projects, resume, and contact information.

The portfolio also includes a secure private admin dashboard for managing messages submitted through the contact form.

---

## About Me

I am a Computer Applications graduate currently pursuing a **Master of Computer Applications (MCA) in Data Science**.

My current areas of interest include:

- Python Development
- Software Development
- Backend Development
- Web Development
- Data Science
- Database Systems

I enjoy building practical applications and continuously improving my programming, problem-solving, and software development skills.

---

## Portfolio Features

- Responsive dark-themed user interface
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

## Backend Features

- Python Flask backend
- SQLite database
- Contact message storage
- Server-side form validation
- Email validation
- Environment-based configuration
- CSRF protection
- Request rate limiting

---

## Admin Dashboard

The portfolio includes a private administration panel for managing contact submissions.

Features include:

- Secure admin authentication
- Hashed password verification
- Session-based login
- Contact message dashboard
- View submitted messages
- Reply through email
- Delete messages
- Secure POST-based logout
- CSRF-protected actions
- Login rate limiting

---

# Featured Project

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

# Technical Skills

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

# Project Structure

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

The following files are intentionally excluded from GitHub:

```text
.env
.venv/
portfolio.db
__pycache__/
.vscode/
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/hanwant26/Hanwant_Portfolio.git
```

## 2. Enter the project directory

```bash
cd Hanwant_Portfolio
```

## 3. Create a virtual environment

On Windows:

```bash
py -m venv .venv
```

## 4. Activate the virtual environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD_HASH=your-generated-password-hash
FLASK_DEBUG=1
```

Never upload your `.env` file to GitHub.

---

# Generate Admin Password Hash

Generate a password hash using:

```bash
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('YOUR_PASSWORD'))"
```

Copy the generated value into:

```env
ADMIN_PASSWORD_HASH=your-generated-hash
```

The actual admin password should never be stored directly in the source code.

---

# Run Locally

Start the Flask application:

```bash
python app.py
```

Open the portfolio:

```text
http://127.0.0.1:5000
```

Admin login:

```text
http://127.0.0.1:5000/admin/login
```

---

# Database

The portfolio currently uses **SQLite**.

The local database file is:

```text
portfolio.db
```

It contains the contact messages submitted through the portfolio.

The database currently stores:

```text
Name
Email
Subject
Message
```

The admin dashboard reads these records and allows them to be viewed or deleted.

`portfolio.db` is excluded from GitHub to prevent contact submissions from being uploaded publicly.

---

# Security

The project currently includes:

- Hashed admin password authentication
- Environment variables for sensitive configuration
- CSRF protection
- POST-based admin logout
- CSRF-protected delete operations
- Server-side input validation
- Email format validation
- Input length limits
- Admin login rate limiting
- Contact form rate limiting
- HTTPOnly session cookies
- SameSite session protection
- Git exclusion of secrets and database records

Additional production-specific security configuration will be applied when the application is deployed.

---

# Education

## Master of Computer Applications — Data Science

**Lovely Professional University**

2026 — Present

---

## Bachelor of Computer Applications — BCA (Science)

**Progressive Education Society's Modern College of Arts, Science and Commerce, Pune**

2022 — 2025

---

# Contact

**Hanwant Singh**

### GitHub

https://github.com/hanwant26

### LinkedIn

https://www.linkedin.com/in/hanwant-singh

### Email

singhhanwant325@gmail.com

---

# Portfolio Repository

https://github.com/hanwant26/Hanwant_Portfolio

---

# Project Status

The portfolio is actively maintained.

More projects and improvements will be added as I continue learning and building new applications.

---

# License

This project is intended for personal portfolio and educational use.

© 2026 Hanwant Singh