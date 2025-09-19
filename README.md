\📌 Flask Project Manager

A simple project & task management application built with Flask, SQLAlchemy, Flask-Login, and Bootstrap.
Users can register, create projects, add tasks, and mark them as done/pending.

🚀 Features

User authentication (Register, Login, Logout)

Project creation & management

Task creation, update (mark as done/pending)

Bootstrap UI with a responsive navbar

SQLite database with Flask-Migrate

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/flask-project-manager.git
cd flask-project-manager

2. Create a Virtual Environment
python -m venv env


Activate it:

Windows:

env\Scripts\activate


Linux/Mac:

source env/bin/activate

3. Install Requirements
pip install -r requirements.txt

4. Set Environment Variables

Update the database URI for PostgreSQL in your environment:

Windows (PowerShell):

set FLASK_APP=app
set FLASK_ENV=development
set DATABASE_URL=postgresql://username:password@localhost:5432/flask_db


Linux/Mac (Bash):

export FLASK_APP=app
export FLASK_ENV=development
export DATABASE_URL=postgresql://username:password@localhost:5432/flask_db


⚠️ Replace username, password, and flask_db with your PostgreSQL credentials and database name.

5. Initialize the Database

Make sure PostgreSQL is running, then run:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

6. Run the Flask App
flask run


👉 App will run at: http://127.0.0.1:5000


✅ Requirements

Python 3.9+

Flask

Flask-SQLAlchemy

Flask-Migrate

Flask-Login

psycopg2-binary (for PostgreSQL driver)

🛠️ Development Notes:

Default DB URI: postgresql://username:password@localhost:5432/flask_db

To reset DB:

flask db downgrade base
flask db upgrade

Home Page:

<img width="959" height="437" alt="homepage" src="https://github.com/user-attachments/assets/433ac9e8-8d57-4507-b654-06cb0bb5fdb6" />




Login Page:

<img width="959" height="426" alt="loginpage" src="https://github.com/user-attachments/assets/b53f9b22-ba6d-4cef-be36-73be18b46d12" />




Project dashboard:

<img width="959" height="427" alt="projects_dashboard" src="https://github.com/user-attachments/assets/9f8ec128-b28c-4721-b283-36a7f5276966" />



Task detail:

<img width="959" height="428" alt="task_details" src="https://github.com/user-attachments/assets/b556d46f-e8f5-4f8c-82a7-1bd9b32fda80" />



