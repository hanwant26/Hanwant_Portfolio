from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

import sqlite3
import os
from functools import wraps
from dotenv import load_dotenv


# =========================
# LOAD ENVIRONMENT VARIABLES
# =========================

load_dotenv()


# =========================
# FLASK APPLICATION
# =========================

app = Flask(__name__)

app.secret_key = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)


# =========================
# ADMIN DETAILS
# =========================

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


# =========================
# DATABASE
# =========================

DATABASE = "portfolio.db"


def get_database_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def create_database():

    connection = get_database_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


create_database()


# =========================
# ADMIN LOGIN REQUIRED
# =========================

def login_required(function):

    @wraps(function)
    def decorated_function(*args, **kwargs):

        if not session.get("admin_logged_in"):

            flash("Please login to access the admin dashboard.")

            return redirect(url_for("admin_login"))

        return function(*args, **kwargs)

    return decorated_function


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return render_template("index.html")


# =========================
# CONTACT FORM
# =========================

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "").strip()

    email = request.form.get("email", "").strip()

    subject = request.form.get("subject", "").strip()

    message = request.form.get("message", "").strip()


    if not name or not email or not subject or not message:

        flash("Please fill in all fields.")

        return redirect(
            url_for("home") + "#contact"
        )


    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO messages (
            name,
            email,
            subject,
            message
        )
        VALUES (?, ?, ?, ?)
    """, (
        name,
        email,
        subject,
        message
    ))


    connection.commit()

    connection.close()


    flash(
        "Your message has been sent successfully!"
    )


    return redirect(
        url_for("home") + "#contact"
    )


# =========================
# ADMIN LOGIN
# =========================

@app.route(
    "/admin/login",
    methods=["GET", "POST"]
)
def admin_login():

    if session.get("admin_logged_in"):

        return redirect(
            url_for("admin_dashboard")
        )


    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )


        if (
            username == ADMIN_USERNAME
            and password == ADMIN_PASSWORD
        ):

            session["admin_logged_in"] = True

            session["admin_username"] = username


            flash(
                "Login successful."
            )


            return redirect(
                url_for("admin_dashboard")
            )


        flash(
            "Invalid username or password."
        )


    return render_template(
        "admin_login.html"
    )


# =========================
# ADMIN DASHBOARD
# =========================

@app.route("/admin")
@login_required
def admin_dashboard():

    connection = get_database_connection()


    messages = connection.execute("""
        SELECT *
        FROM messages
        ORDER BY id DESC
    """).fetchall()


    connection.close()


    return render_template(
        "admin_dashboard.html",
        messages=messages
    )


# =========================
# DELETE MESSAGE
# =========================

@app.route(
    "/admin/delete/<int:message_id>",
    methods=["POST"]
)
@login_required
def delete_message(message_id):

    connection = get_database_connection()


    connection.execute(
        """
        DELETE FROM messages
        WHERE id = ?
        """,
        (message_id,)
    )


    connection.commit()

    connection.close()


    flash(
        "Message deleted successfully."
    )


    return redirect(
        url_for("admin_dashboard")
    )


# =========================
# ADMIN LOGOUT
# =========================

@app.route("/admin/logout")
@login_required
def admin_logout():

    session.clear()


    flash(
        "You have been logged out."
    )


    return redirect(
        url_for("admin_login")
    )


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":

    app.run(debug=True)