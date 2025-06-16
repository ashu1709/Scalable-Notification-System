# 🚀 Assist Notifier

A clean, scalable, and production-ready **notification system** built with **FastAPI**.  
Receives webhook requests (like from a bot) and dispatches notifications to different channels (e.g., Slack, Email) based on the topic.  
Designed with professional architecture, ready for real-world use.

---

## ✨ Features

✅ **FastAPI** with async endpoints  
✅ **Dispatcher pattern** for topic-based routing  
✅ **Slack and Email channels (mocked)** for extensibility  
✅ **Database persistence** (SQLite by default) using SQLAlchemy  
✅ **Admin Panel** with Bootstrap + auto-refresh  
✅ **Logging** to console and file  
✅ **Environment configuration** via `.env` and `python-dotenv`  
✅ **Testing**: unit & integration with `pytest` and `httpx`  
✅ **Type-checked** with `mypy`  
✅ **Linted & formatted** with `ruff` and `black`  
✅ **Alembic** migrations for DB version control  
✅ **Docker-ready**  
✅ **Clean architecture** with separation of concerns: API, services, repository, db, etc.

---

![image](https://github.com/user-attachments/assets/c11e5f49-972e-4022-ab09-4d02fc624a2f)
![image](https://github.com/user-attachments/assets/16feac06-dc35-43c8-aeb6-0b403a92bfcd)
![image](https://github.com/user-attachments/assets/5c035d49-a32a-41b2-9995-bba9b1a3f825)

---

## 📦 Technologies Used

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **Jinja2** for templates
- **Pipenv**
- **Docker**
- **GitHub Actions** (CI-ready)

## Running locally

```bash
docker build -t assist-notifier .
docker run --env-file .env -p 8000:8000 --name assist-notifier assist-notifier
```
