# Student Management System (Django Template-Based)

## 1. Project Overview
This project is a web-based Student Management System built using Django and HTML templates.  
It allows managing Teachers, Courses, Students, and Grades with full Create, Read, Update, and Delete (CRUD) functionality.

The goal is to understand Django MVC (Model–View–Template) architecture and database relationships.

---

## 2. Technologies Used
- Python
- Django Framework
- SQLite Database (default)
- HTML, CSS (Templates)
- Bootstrap (optional styling)

---

## 3. Database Models and Relationships

| Model   | Fields | Relationships |
|--------|--------|---------------|
| **Teacher** | name, email (unique) | One Teacher → Many Courses |
| **Course** | name, code (unique), teacher (FK to Teacher) | A course is taught by one Teacher |
| **Student** | name, email (unique), courses (Many-to-Many) | A student can enroll in multiple courses |
| **Grade** | student (FK), course (FK), score (0–100) | One Student → Many Grades, unique(student, course) |

### Relationship Summary
- **Teacher → Course** → One-to-Many
- **Student ↔ Course** → Many-to-Many
- **Student → Grade → Course** → One-to-Many (with uniqueness constraint)

---

## 4. Validations

### Model-Level Validation
- Email fields are **unique**.
- Grade `score` must be **between 0 and 100**.
- A student can have **only one grade per course** (unique constraint).

### View-Level Validation
- While adding a grade, ensure **the student is enrolled in the selected course**.

---

## 5. Features & Pages (CRUD)

| Feature | Actions Available |
|--------|------------------|
| **Students** | Add, View List, Update, Delete, View Details (including enrolled courses and average score) |
| **Courses** | Add, View List, Update, Delete |
| **Grades** | Add, View, Update, Delete (with validation checks) |

---

## 6. Installation & Setup

```bash
git clone https://github.com/Hr-max-star/student_management_system.git
cd student_management_system
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
