from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from flask_wtf.csrf import CSRFProtect

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from werkzeug.security import check_password_hash

from psycopg.rows import dict_row

import psycopg
import sqlite3
import os
import re

from functools import wraps
from dotenv import load_dotenv


# =========================
# LOAD ENVIRONMENT
# =========================

load_dotenv()


# =========================
# FLASK APPLICATION
# =========================

app = Flask(__name__)


# =========================
# ENVIRONMENT VARIABLES
# =========================

SECRET_KEY = os.getenv("SECRET_KEY")

ADMIN_USERNAME = os.getenv(
    "ADMIN_USERNAME"
)

ADMIN_PASSWORD_HASH = os.getenv(
    "ADMIN_PASSWORD_HASH"
)

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)


if not SECRET_KEY:

    raise RuntimeError(
        "SECRET_KEY is missing."
    )


if not ADMIN_USERNAME:

    raise RuntimeError(
        "ADMIN_USERNAME is missing."
    )


if not ADMIN_PASSWORD_HASH:

    raise RuntimeError(
        "ADMIN_PASSWORD_HASH is missing."
    )


app.secret_key = SECRET_KEY


# =========================
# DATABASE MODE
# =========================

# If DATABASE_URL exists:
#     PostgreSQL will be used.
#
# If DATABASE_URL does not exist:
#     SQLite will be used.

USE_POSTGRES = bool(
    DATABASE_URL
)


SQLITE_DATABASE = os.path.join(
    app.root_path,
    "portfolio.db"
)


# =========================
# CSRF PROTECTION
# =========================

csrf = CSRFProtect(app)


# =========================
# RATE LIMITING
# =========================

RATE_LIMIT_STORAGE = os.getenv(
    "RATELIMIT_STORAGE_URI",
    "memory://"
)


limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    storage_uri=RATE_LIMIT_STORAGE
)


# =========================
# SESSION SECURITY
# =========================

app.config[
    "SESSION_COOKIE_HTTPONLY"
] = True


app.config[
    "SESSION_COOKIE_SAMESITE"
] = "Lax"


# Locally:
# SESSION_COOKIE_SECURE=0
#
# Production:
# SESSION_COOKIE_SECURE=1

app.config[
    "SESSION_COOKIE_SECURE"
] = (
    os.getenv(
        "SESSION_COOKIE_SECURE",
        "0"
    )
    == "1"
)


# =========================
# DATABASE CONNECTION
# =========================

def get_database_connection():

    # -------------------------
    # POSTGRESQL
    # -------------------------

    if USE_POSTGRES:

        connection = psycopg.connect(
            DATABASE_URL,
            row_factory=dict_row
        )

        return connection


    # -------------------------
    # SQLITE
    # -------------------------

    connection = sqlite3.connect(
        SQLITE_DATABASE
    )

    connection.row_factory = (
        sqlite3.Row
    )

    return connection


# =========================
# CREATE DATABASE TABLE
# =========================

def create_database():

    connection = (
        get_database_connection()
    )


    try:

        # =====================
        # POSTGRESQL TABLE
        # =====================

        if USE_POSTGRES:

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS messages (
                    id BIGSERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(150) NOT NULL,
                    subject VARCHAR(150) NOT NULL,
                    message TEXT NOT NULL,
                    created_at TIMESTAMP
                        DEFAULT CURRENT_TIMESTAMP
                )
                """
            )


        # =====================
        # SQLITE TABLE
        # =====================

        else:

            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    message TEXT NOT NULL,
                    created_at TIMESTAMP
                        DEFAULT CURRENT_TIMESTAMP
                )
                """
            )


        connection.commit()


    finally:

        connection.close()


create_database()


# =========================
# EMAIL VALIDATION
# =========================

def is_valid_email(email):

    pattern = (
        r"^[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}$"
    )


    return re.match(
        pattern,
        email
    ) is not None


# =========================
# LOGIN REQUIRED
# =========================

def login_required(function):

    @wraps(function)
    def decorated_function(
        *args,
        **kwargs
    ):

        if not session.get(
            "admin_logged_in"
        ):

            flash(
                "Please login to access "
                "the admin dashboard."
            )


            return redirect(
                url_for(
                    "admin_login"
                )
            )


        return function(
            *args,
            **kwargs
        )


    return decorated_function


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =========================
# CONTACT FORM
# =========================

@app.route(
    "/contact",
    methods=["POST"]
)
@limiter.limit(
    "5 per minute; 20 per hour"
)
def contact():

    name = request.form.get(
        "name",
        ""
    ).strip()


    email = request.form.get(
        "email",
        ""
    ).strip()


    subject = request.form.get(
        "subject",
        ""
    ).strip()


    message = request.form.get(
        "message",
        ""
    ).strip()


    # =========================
    # EMPTY FIELD VALIDATION
    # =========================

    if (
        not name
        or not email
        or not subject
        or not message
    ):

        flash(
            "Please fill in all fields."
        )


        return redirect(
            url_for("home")
            + "#contact"
        )


    # =========================
    # LENGTH VALIDATION
    # =========================

    if len(name) > 100:

        flash(
            "Name is too long."
        )


        return redirect(
            url_for("home")
            + "#contact"
        )


    if len(email) > 150:

        flash(
            "Email address is too long."
        )


        return redirect(
            url_for("home")
            + "#contact"
        )


    if len(subject) > 150:

        flash(
            "Subject is too long."
        )


        return redirect(
            url_for("home")
            + "#contact"
        )


    if len(message) > 2000:

        flash(
            "Message must be under "
            "2000 characters."
        )


        return redirect(
            url_for("home")
            + "#contact"
        )


    # =========================
    # EMAIL VALIDATION
    # =========================

    if not is_valid_email(
        email
    ):

        flash(
            "Please enter a valid "
            "email address."
        )


        return redirect(
            url_for("home")
            + "#contact"
        )


    # =========================
    # SAVE MESSAGE
    # =========================

    connection = (
        get_database_connection()
    )


    try:

        # ---------------------
        # POSTGRESQL
        # ---------------------

        if USE_POSTGRES:

            connection.execute(
                """
                INSERT INTO messages (
                    name,
                    email,
                    subject,
                    message
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    name,
                    email,
                    subject,
                    message
                )
            )


        # ---------------------
        # SQLITE
        # ---------------------

        else:

            connection.execute(
                """
                INSERT INTO messages (
                    name,
                    email,
                    subject,
                    message
                )
                VALUES (
                    ?,
                    ?,
                    ?,
                    ?
                )
                """,
                (
                    name,
                    email,
                    subject,
                    message
                )
            )


        connection.commit()


    finally:

        connection.close()


    flash(
        "Your message has been "
        "sent successfully!"
    )


    return redirect(
        url_for("home")
        + "#contact"
    )


# =========================
# ADMIN LOGIN
# =========================

@app.route(
    "/admin/login",
    methods=["GET", "POST"]
)
@limiter.limit(
    "5 per minute",
    methods=["POST"]
)
def admin_login():

    if session.get(
        "admin_logged_in"
    ):

        return redirect(
            url_for(
                "admin_dashboard"
            )
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


        username_correct = (
            username
            == ADMIN_USERNAME
        )


        password_correct = (
            check_password_hash(
                ADMIN_PASSWORD_HASH,
                password
            )
        )


        if (
            username_correct
            and password_correct
        ):

            session.clear()


            session[
                "admin_logged_in"
            ] = True


            session[
                "admin_username"
            ] = username


            flash(
                "Login successful."
            )


            return redirect(
                url_for(
                    "admin_dashboard"
                )
            )


        flash(
            "Invalid username "
            "or password."
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

    connection = (
        get_database_connection()
    )


    try:

        messages = (
            connection.execute(
                """
                SELECT
                    id,
                    name,
                    email,
                    subject,
                    message,
                    created_at
                FROM messages
                ORDER BY id DESC
                """
            )
            .fetchall()
        )


    finally:

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
def delete_message(
    message_id
):

    connection = (
        get_database_connection()
    )


    try:

        # ---------------------
        # POSTGRESQL
        # ---------------------

        if USE_POSTGRES:

            connection.execute(
                """
                DELETE FROM messages
                WHERE id = %s
                """,
                (
                    message_id,
                )
            )


        # ---------------------
        # SQLITE
        # ---------------------

        else:

            connection.execute(
                """
                DELETE FROM messages
                WHERE id = ?
                """,
                (
                    message_id,
                )
            )


        connection.commit()


    finally:

        connection.close()


    flash(
        "Message deleted successfully."
    )


    return redirect(
        url_for(
            "admin_dashboard"
        )
    )


# =========================
# ADMIN LOGOUT
# =========================

@app.route(
    "/admin/logout",
    methods=["POST"]
)
@login_required
def admin_logout():

    session.clear()


    flash(
        "You have been logged out."
    )


    return redirect(
        url_for(
            "admin_login"
        )
    )


# =========================
# RATE LIMIT ERROR
# =========================

@app.errorhandler(429)
def rate_limit_exceeded(
    error
):

    return render_template(
        "429.html"
    ), 429


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":

    debug_mode = (
        os.getenv(
            "FLASK_DEBUG",
            "0"
        )
        == "1"
    )


    database_name = (
        "PostgreSQL"
        if USE_POSTGRES
        else "SQLite"
    )


    print(
        f"Database: {database_name}"
    )


    app.run(
        debug=debug_mode
    )