# 📰 CodeZone

**CodeZone** is a simple Django-powered platform where registered users can publish articles and leave reviews on programming topics.

🚀 Live Demo: [javid777.pythonanywhere.com](https://javid777.pythonanywhere.com/)


---

## 📌 Features

- 📝 Add and display programming articles
- 💬 Leave reviews (only if authenticated)
- 🔐 Registration & Login system
- 🧑‍💻 Admin panel for content and user management
- 🎨 Minimal custom frontend with emojis
- ☁️ Deployed on [PythonAnywhere](https://www.pythonanywhere.com/)  

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (local), auto-loaded on deploy
- **Deployment**: Railway (Procfile, collectstatic, loaddata)
- **Frontend**: Django templates, custom CSS

---

## ⚙️ Installation (Local)

```bash
git clone https://github.com/your-username/articles_catalog.git
cd articles_catalog

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations and load sample data (optional)
python manage.py migrate
python manage.py loaddata data.json

# Create admin (if needed)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

---

## 📁 Project Structure

```
articles_catalog/
├── articles_catalog/     # Django settings
├── main/                 # App with articles and reviews
├── static/               # Static files (CSS, images)
├── templates/            # HTML templates
├── data.json             # Preloaded data (articles, users, reviews)
├── db.sqlite3            # Local database (optional)
├── manage.py
├── Procfile
└── requirements.txt
```

---

## 👨‍💻 Admin Access

You can access the admin panel at:

**`/admin/`**

> If you use `data.json`, login credentials will already be included.

---

## 📄 License

MIT License. Free for personal or commercial use.

---

Made with ❤️ by Javid Mustafayev
