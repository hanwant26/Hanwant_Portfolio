# Hanwant Singh — Personal Portfolio

A modern, responsive personal portfolio website built with **Python and Flask** to showcase my skills, education, projects, resume, and contact information.

The portfolio also includes a private admin dashboard for managing messages submitted through the contact form.

---

## About Me

I am a Computer Applications graduate currently pursuing a **Master of Computer Applications (MCA) in Data Science**.

I am interested in:

- Python Development
- Software Development
- Web Development
- Data Science
- Backend Development
- Database Systems

I enjoy building practical applications and continuously improving my programming, problem-solving, and software development skills.

---

## Features

### Portfolio

- Responsive modern dark UI
- Animated hero section
- Dynamic typing animation
- About section
- Technical skills section
- Featured projects
- Education timeline
- Resume viewer
- GitHub and LinkedIn integration
- Contact form
- Scroll reveal animations
- Active navigation highlighting
- Mobile hamburger navigation
- Back-to-top button
- Custom favicon
- SEO metadata
- Social sharing metadata

### Backend

- Flask application
- SQLite database
- Contact message storage
- Server-side form validation
- Email format validation
- CSRF protection
- Request rate limiting
- Environment-based configuration

### Admin Dashboard

- Secure admin login
- Password hashing
- Session-based authentication
- Private message dashboard
- View contact submissions
- Reply through email
- Delete messages
- Secure logout
- CSRF-protected admin actions
- Login rate limiting

---

## Featured Project

### MeetVerse

MeetVerse is a real-time video conferencing platform built using Python and Django.

Features include:

- Real-time video conferencing
- Room-based communication
- Persistent meeting chat
- Dynamic participant tracking
- Live meeting timer
- Secure room creation

**Technologies**

`Python` `Django` `LiveKit` `SQLite` `JavaScript` `HTML5` `CSS3`

Repository:

https://github.com/hanwant26/MeetVerse

---

## Technologies Used

### Programming

- Python
- SQL
- JavaScript
- C++
- Shell Scripting

### Web Development

- Flask
- Django
- HTML5
- CSS3
- Bootstrap
- REST APIs

### Databases

- MySQL
- SQLite

### Tools

- Git
- GitHub
- Linux
- VS Code
- VirtualBox

---

## Project Structure

```text
Hanwant_Portfolio/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
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
└── portfolio.db
```

> `.env`, `.venv`, and `portfolio.db` are excluded from GitHub using `.gitignore`.

---

## Installation

### 1. Clone the repository

```bash
git clone YOUR_PORTFOLIO_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Hanwant_Portfolio
```

### 3. Create a virtual environment

Windows:

```bash
py -m venv .venv
```

### 4. Activate the environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD_HASH=your-password-hash
FLASK_DEBUG=1
```

Never commit your `.env` file to GitHub.

---

## Generate an Admin Password Hash

Run:

```bash
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('YOUR_PASSWORD'))"
```

Copy the generated hash into:

```env
ADMIN_PASSWORD_HASH=
```

Do not store your normal admin password directly in `.env`.

---

## Run Locally

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Admin login:

```text
http://127.0.0.1:5000/admin/login
```

---

## Security

The application currently includes:

- Hashed admin password authentication
- Environment variables for sensitive configuration
- CSRF protection
- Secure POST-based logout
- CSRF-protected delete operations
- Server-side input validation
- Contact message length validation
- Admin login rate limiting
- Contact form rate limiting
- HTTPOnly session cookies
- SameSite session protection

Additional production configuration will be applied before deployment.

---

## Education

### Master of Computer Applications — Data Science

**Lovely Professional University**

2026 — Present

### Bachelor of Computer Applications — BCA (Science)

**Progressive Education Society's Modern College of Arts, Science and Commerce, Pune**

2022 — 2025

---

## Contact

**Hanwant Singh**

GitHub  
https://github.com/hanwant26

LinkedIn  
https://www.linkedin.com/in/hanwant-singh

Email  
singhhanwant325@gmail.com

---

## Status

The portfolio is actively maintained.

More projects and improvements will be added as I continue developing my skills and building new applications.

---

## License

This project is intended for personal portfolio use.

© 2026 Hanwant Singh