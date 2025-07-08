# 📝 Personal Blog

A simple personal blog platform built with Flask, providing functionality for users to **create**, **read**, **update**, and **delete** blog posts. The application supports user **authentication**, session management, and basic access control using Flask sessions.

---

## 🚀 Features

* 🧑‍💻 User Authentication (Login/Logout)
* 📬 Flash Messaging
* 📜 Blog Post CRUD (Create, Read, Update, Delete)
* ✅ Form Validation with Flask-WTF
* 🧱 Template Inheritance with Jinja2
* 🔒 Route Protection for Authenticated Users
* 💲 SQLite Database with SQLAlchemy ORM

---

## 🧰 Tech Stack

| Layer       | Technology          |
| ----------- | ------------------- |
| Backend     | Python (Flask)      |
| ORM         | SQLAlchemy          |
| Forms       | Flask-WTF           |
| Templates   | Jinja2              |
| Styling     | Bootstrap (via CDN) |
| Database    | SQLite              |
| Environment | python-dotenv       |

---

## 📁 Project Structure

```
personal_blog/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   ├── forms.py
│   ├── utils.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── create_blog.html
│       ├── blog_details.html
│       └── update_blog.html
├── static/
│   └── style.css
├── config.py
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/personal_blog.git
cd personal_blog
```

### 2. Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and update values:

```env
DEBUG=True
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///app.db

ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=yourpassword
```

### 5. Run the application

```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🔡 Authentication Notes

* The app uses a hardcoded admin user defined in `.env`.
* Session-based authentication stores the `user_id` in Flask's session.
* Protected routes require login via a `login_required` decorator.
