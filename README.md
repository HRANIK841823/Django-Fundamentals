# Django Fundamentals 🚀

A beginner-friendly repository for learning and practicing the **fundamentals of Django**, the popular Python web framework for building secure and scalable web applications.

This repository contains practical examples and exercises covering Django's core concepts, project structure, URL routing, views, templates, models, forms, database operations, and CRUD functionality.

---

## 📌 Project Overview

The goal of this project is to build a strong foundation in Django by learning its core components step by step through practical implementation.

### Topics Covered

* Django installation and setup
* Django project and app structure
* URL routing
* Views
* Templates
* Template inheritance
* Static files
* Dynamic URLs
* Models
* Django ORM
* Database operations
* Forms
* Model Forms
* CRUD Operations
* Admin Panel
* Migrations
* HTTP methods
* Request and Response handling
* Django application structure

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML**
* **CSS**
* **Git & GitHub**

---

## 📂 Project Structure

```text
Django-Fundamentals/
│
├── manage.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

> The exact structure may change as new Django concepts and applications are added.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HRANIK841823/Django-Fundamentals.git
```

### 2. Navigate to the Project

```bash
cd Django-Fundamentals
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django
```

---

## ▶️ Run the Development Server

Apply migrations first:

```bash
python manage.py migrate
```

Then start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🗄️ Database & Migrations

Django provides a powerful ORM that allows us to interact with databases using Python objects instead of writing SQL manually.

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

View migration status:

```bash
python manage.py showmigrations
```

---

## 👨‍💻 Django Admin Panel

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the server:

```bash
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/admin/
```

The Django Admin Panel provides an easy interface for managing database records.

---

## 🔄 CRUD Operations

This project also focuses on the basic CRUD operations:

| Operation  | Description               |
| ---------- | ------------------------- |
| **Create** | Add new records           |
| **Read**   | Retrieve existing records |
| **Update** | Modify existing records   |
| **Delete** | Remove records            |

Example Django ORM operations:

```python
# Create
Product.objects.create(
    name="Laptop",
    price=80000
)

# Read
products = Product.objects.all()

# Update
product = Product.objects.get(id=1)
product.price = 75000
product.save()

# Delete
product = Product.objects.get(id=1)
product.delete()
```

---

## 🎯 Learning Objectives

After completing this project, I aim to understand:

* How Django projects are structured
* How Django applications work
* How URL routing works
* How views process requests
* How templates generate HTML
* How Django ORM communicates with databases
* How models represent database tables
* How forms handle user input
* How CRUD applications are implemented
* How Django Admin works
* How migrations manage database changes

---

## 🚀 Future Improvements

The project may be expanded with:

* User Authentication
* Registration & Login
* Django REST Framework
* REST APIs
* JWT Authentication
* PostgreSQL
* File & Image Upload
* Class-Based Views
* Advanced ORM Queries
* Pagination
* Search & Filtering
* Deployment

---

## 📚 Learning Approach

This repository is primarily focused on **hands-on Django learning**.

Each concept is implemented practically rather than only studying theory. The project will gradually evolve from basic Django fundamentals into more advanced backend development concepts.

---

## 👤 Author

**HR ANIK**

Computer Science & Engineering Student
Interested in **Python, Django, Machine Learning, AI, and Backend Development**.

---

## ⭐ Support

If you find this repository useful for learning Django, consider giving it a ⭐ on GitHub.

Happy Coding! 💻🐍
