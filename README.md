# 🛠️ User Activity Logger – Django REST Framework Project

This project implements a **User Activity Log** API using Django and Django REST Framework. It includes features such as logging user actions, filtering logs, Redis caching, workflow status transitions, and API security.

---

## 🚀 Features

- Log user activity (LOGIN, LOGOUT, UPLOAD_FILE, etc.)
- Retrieve logs per user
- Filter logs by action and timestamp range
- PATCH API for workflow status (`PENDING`, `IN_PROGRESS`, `DONE`)
- Redis caching for improved performance
- API secured with authentication
- Unit tests for models, views, and caching logic

---

## 🏗️ Technologies Used

- Django
- Django REST Framework
- PostgreSQL (you can use SQLite for local testing)
- Redis (for caching)
- Docker (optional for isolated environment)
- Pytest / Django test client

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/activitylogger.git
cd activitylogger
2. Create and activate virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Setup environment (Optional .env)
Create a .env file for sensitive configs (or set in settings.py directly).

5. Run migrations
bash
Copy
Edit
python manage.py migrate
6. Create superuser (optional)
bash
Copy
Edit
python manage.py createsuperuser
7. Start development server
bash
Copy
Edit
python manage.py runserver
App runs at: http://127.0.0.1:8000/

🔑 API Endpoints
Method	Endpoint	Description
POST	/activity-log/	Create a new user activity log
GET	/activity-log/user/<user_id>/	Get all logs for a user
GET	/activity-log/user/<user_id>/?action=UPLOAD_FILE	Filter by action
GET	/activity-log/user/<user_id>/?start=YYYY-MM-DD&end=YYYY-MM-DD	Filter by timestamp
PATCH	/activity-log/<id>/status/	Update log status

🧪 Running Tests
bash
Copy
Edit
python manage.py test
Includes tests for:

Model creation

POST, GET, PATCH endpoints

Caching logic (mocked if needed)

🔒 Security
All endpoints require authentication

DRF’s IsAuthenticated permission enforced

⚡ Bonus: Redis Caching
GET responses are cached per-user for 1 minute

Cache invalidates when a new log is created

Redis Setup (Linux/Mac)
bash
Copy
Edit
brew install redis      # or use apt-get install redis
redis-server
Make sure Redis is running before starting the Django app.

📦 Requirements
Install with:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

php
Copy
Edit
Django>=3.2
djangorestframework
psycopg2-binary
redis
django-redis
✅ Code Quality
Follows PEP8 conventions

Structured according to Django best practices

📮 Postman Collection (Optional)
You can import the included Postman collection to test endpoints quickly (available on request).

📂 Submission Checklist
 All models and APIs created

 Redis caching implemented

 Status workflow simulated

 Tests written for model, API, and cache

 README included with setup and usage

 requirements.txt provided

👨‍💻 Author
Akshat
Email: akshatpuri00@gmail.com
GitHub: Akshat-Puri