# Commands

# VENV

python3 -m venv venv

source venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt


# Run App

python run.py

# Documentation

{base_url}/api/docs


# Scripts

python scripts/test_env_vars.py

python scripts/db_connection_check.py

python scripts/db_data_collection_and_export.py

python scripts/test_api_endpoints.py


# Testing

pytest

pytest tests/routes

pytest tests/routes/test_todos.py

pytest --cov=app tests/

pytest --cov=app --cov-report=html tests/

