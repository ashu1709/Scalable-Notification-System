📡 Scalable Notification System
A modular and production-grade notification delivery platform built with FastAPI.
It listens for webhook payloads (e.g., from bots or services) and intelligently routes messages to various channels like Slack or Email, based on the incoming topic.

The project follows clean architectural practices and is built for extensibility and real-world deployment.

🔧 Key Features
🚀 Asynchronous FastAPI endpoints for high-performance handling

🔀 Dispatcher-based topic routing for dynamic message targeting

📬 Slack & Email notification channels (mocked for extension)

🗃️ SQLite-backed persistence powered by SQLAlchemy ORM

🧑‍💼 Admin dashboard built with Jinja2 and Bootstrap; supports auto-refresh

📜 Logging to both terminal and log files

⚙️ Environment-driven configuration using .env and python-dotenv

🧪 Comprehensive testing suite using pytest and httpx

🔍 Type-checked using mypy

🧹 Code formatting & linting with black and ruff

🧬 Database migrations using Alembic

🐳 Containerized with Docker

🧱 Layered architecture ensuring separation of concerns across API, services, DB, and repositories


🛠️ Stack & Tools
Tool	Purpose
Python 3.11	Language
FastAPI	Web framework
SQLAlchemy	ORM for DB handling
Alembic	Database versioning
Jinja2	HTML templating
Pipenv	Dependency management
Docker	Containerization
GitHub Actions	CI/CD ready

🚀 Running the Project Locally
bash 

# Build the Docker image
docker build -t scalable-notifier .

# Run the container with environment variables
docker run --env-file .env -p 8000:8000 --name scalable-notifier scalable-notifier
