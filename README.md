# Django Registration System

# Installation

Clone the repository:

Copy code

git clone https://github.com/your-username/django-registration-system.git

cd django-registration-system

Create and activate a virtual environment (optional but recommended):

Copy code

python -m venv venv

venv\Scripts\activate  # On Windows

source venv/bin/activate  # On macOS/Linux

# Install required packages:

bash
Copy code

pip install -r requirements.txt

Apply migrations:

bash

Copy code

python manage.py migrate

Usage

Run the development server:

bash
Copy code

python manage.py runserver

Access the application at http://localhost:8000/.

# URLs
/: Home and signup form

/login/: Login page

/home/: User's dashboard

/logout/: Logout

/referees/: View referees

# Dependencies

Django 3.x

Python 3.x
