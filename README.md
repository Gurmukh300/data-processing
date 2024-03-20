# Data Processing

A web application for processing CSV and displaying data, featuring Pandas data type inference and 
conversion on the Django backend and a React with Tailwind frontend for user interaction.

## Getting Started

### Frontend (React)


cd frontend 
npm install
npm run start


## Backend Django

# Install virtualenv if not installed
pip install virtualenv

# Create a virtual environment
virtualenv env

# Activate the virtual environment
source env/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Run migrations
cd backend
python manage.py migrate

# Start the Django server
python manage.py runserver


# Before running the frontend,
make sure to set the REACT_APP_REST_API_URL environment variable in the .env file to connect the frontend with the backend.

# .env file
REACT_APP_REST_API_URL="http://127.0.0.1:8000/api/data/"
