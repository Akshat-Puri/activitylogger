1. Setup Instructions

    pip install -r requirements.txt

    python manage.py migrate

    python manage.py runserver


2. Sample API Calls

    POST /activity-log/

    GET /activity-log/user/<id>?action=LOGIN

    PATCH /activity-log/<id>/status/


3. Note: Follow PEP8 using flake8