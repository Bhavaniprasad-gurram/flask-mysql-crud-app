-- Student Management System - database schema
-- Run this file in MySQL before starting the Flask app.

CREATE DATABASE IF NOT EXISTS flask_crud_db;
USE flask_crud_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample row
INSERT INTO students (name, email, course)
VALUES ('Sample Student', 'sample@example.com', 'Python Full Stack');
