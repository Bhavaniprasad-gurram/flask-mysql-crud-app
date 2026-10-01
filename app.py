"""
Student Management System - Flask + MySQL CRUD App

A simple full-stack CRUD application built with Flask and MySQL.
Features: Add, View, Edit and Delete student records.

Setup:
    1. Install dependencies:  pip install -r requirements.txt
    2. Create the database:   run schema.sql in MySQL
    3. Set environment variables (or edit DB_CONFIG below):
       DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
    4. Run:  python app.py
"""

import os

import mysql.connector
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "flask_crud_db"),
}


def get_db_connection():
    """Create and return a new MySQL database connection."""
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
    """Show all students."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students ORDER BY id")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    """Add a new student."""
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        course = request.form["course"].strip()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
            (name, email, course),
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Student added successfully!")
        return redirect(url_for("index"))
    return render_template("add_student.html")


@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    """Edit an existing student."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        course = request.form["course"].strip()
        cursor.execute(
            "UPDATE students SET name=%s, email=%s, course=%s WHERE id=%s",
            (name, email, course, student_id),
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Student updated successfully!")
        return redirect(url_for("index"))
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("edit_student.html", student=student)


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    """Delete a student."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Student deleted successfully!")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
