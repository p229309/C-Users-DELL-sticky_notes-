# 📝 Django Sticky Notes App

A simple and user-friendly **Sticky Notes web application** built using **Django**.
Users can create, update, delete, and manage their personal notes securely with authentication.

---

## 🚀 Features

* 🔐 User Authentication (Login / Logout)
* 📝 Create Notes
* 📋 View All Notes
* ✏️ Update Notes
* ❌ Delete Notes
* 👤 User-specific Notes (each user sees only their notes)
* 🎨 Basic UI using Bootstrap

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, Bootstrap
* **Database:** SQLite (default Django DB)

---

## 📁 Project Structure

```
sticky_notes/
│── manage.py
│
├── sticky_notes/
│   ├── settings.py
│   ├── urls.py
│
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── registration/login.html
│
├── notes/templates/notes/
│   ├── note_list.html
│   ├── create_note.html
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/sticky-notes.git
cd sticky-notes
```

### 2. Create virtual environment

```
python -m venv env
```

### 3. Activate environment

**Windows:**

```
env\Scripts\activate
```

**Linux/Mac:**

```
source env/bin/activate
```

### 4. Install dependencies

```
pip install django
```

### 5. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```
python manage.py createsuperuser
```

### 7. Run server

```
python manage.py runserver
```

---

## 🌐 Usage

* Open browser: `http://127.0.0.1:8000/`
* Login using your account
* Create and manage your notes

---

## 📌 URLs

| URL             | Description |
| --------------- | ----------- |
| `/`             | View notes  |
| `/create/`      | Create note |
| `/update/<id>/` | Update note |
| `/delete/<id>/` | Delete note |
| `/login/`       | Login       |
| `/logout/`      | Logout      |
| `/admin/`       | Admin panel |

---

## 🧠 Future Improvements

* 🎨 Better UI (Sticky Notes Design)
* 🔍 Search functionality
* 📌 Pin important notes
* 📱 REST API (Django REST Framework)
* 🤖 AI-based note summarization

---

## 👨‍💻 Author

**M Abdul Rehman**
Software Engineering Student

---

## ⭐ Contribution

Feel free to fork this repo and improve it!

---

## 📄 License

This project is open-source and free to use.
