# Student Management System — Flask + MySQL CRUD App

A simple full-stack CRUD web application built with **Flask** and **MySQL**.
It lets you add, view, edit, and delete student records stored in a MySQL database.

## Features
- View all students in a table
- Add a new student (name, email, course)
- Edit existing student details
- Delete a student with confirmation
- Flash messages for add / update / delete actions

## Tech Stack
- **Backend:** Python, Flask
- **Database:** MySQL (mysql-connector-python)
- **Frontend:** HTML, CSS, Jinja2 templates

## Project Structure
```
flask-mysql-crud-app/
├── app.py                  # Flask app with all CRUD routes
├── requirements.txt        # Python dependencies
├── schema.sql              # Database + table creation script
├── templates/
│   ├── base.html           # Common layout
│   ├── index.html          # Student list
│   ├── add_student.html    # Add form
│   └── edit_student.html   # Edit form
└── static/
    └── style.css           # Styling
```

## Setup & Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/Bhavaniprasad-gurram/flask-mysql-crud-app.git
   cd flask-mysql-crud-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database** — run `schema.sql` in MySQL:
   ```bash
   mysql -u root -p < schema.sql
   ```

4. **Configure the database connection** (optional — defaults work for local MySQL):
   ```bash
   export DB_HOST=localhost
   export DB_USER=root
   export DB_PASSWORD=your_password
   export DB_NAME=flask_crud_db
   ```

5. **Run the app**
   ```bash
   python app.py
   ```
   Open http://127.0.0.1:5000 in your browser.

## Future Improvements
- Form validation and duplicate-email handling
- Search and pagination for the student list
- Login / authentication
- REST API version of the CRUD endpoints
