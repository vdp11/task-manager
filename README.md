# 🗂️ Django Task Manager

A simple yet powerful task management web application built with Django.  
It allows users to create, view, update, and delete tasks through a clean web interface and Django admin panel.

---

## 🚀 Features

- Create new tasks
- View all tasks in a dashboard
- Edit existing tasks
- Delete tasks
- Django Admin integration
- SQLite database (default)
- CSRF protection enabled
- Clean MVC architecture (Models, Views, Templates)

---

## 🛠️ Tech Stack

- Python 3.12+
- Django 6.x
- SQLite3
- HTML5 (Django Templates)
- CSS (basic styling)

---

## 📁 Project Structure
task_manager/
│
├── task_manager/ # Project settings
├── tasksapp/ # Main app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ ├── templates/
│ └── tasksapp/
│ ├── myfirst.html
│ └── edit_task.html
├── db.sqlite3
├── manage.py
└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager

python3 -m venv venv
source venv/bin/activate

pip install django

python manage.py makemigrations
python manage.py migrate

🌐 Usage
Visit: http://127.0.0.1:8000/tasksapp/
Admin panel: http://127.0.0.1:8000/admin/
