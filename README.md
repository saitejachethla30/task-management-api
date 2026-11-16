
# Task Management REST API

## Project Overview
A Task Management REST API developed using Django REST Framework. It allows users to register, log in, and manage their personal tasks securely using JWT authentication.

## Technologies Used
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman

## Features
- User Registration
- User Login
- JWT Authentication
- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks
- User-specific task access
- Password hashing

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/register/ | Register user |
| POST | /api/login/ | Login and get tokens |
| POST | /api/token/refresh/ | Refresh access token |
| GET | /api/tasks/ | View tasks |
| POST | /api/tasks/ | Create task |
| GET | /api/tasks/{id}/ | View one task |
| PUT | /api/tasks/{id}/ | Update task |
| PATCH | /api/tasks/{id}/ | Partially update task |
| DELETE | /api/tasks/{id}/ | Delete task |

## Authentication
This project uses JWT authentication.

Add the access token in the Authorization header:

Bearer YOUR_ACCESS_TOKEN

## Installation and Setup

1. Clone the repository.
2. Open the project folder.
3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

5. Install dependencies:

   pip install -r requirements.txt

6. Run database migrations:

   python manage.py migrate

7. Start the development server:

   python manage.py runserver

## Testing
All API endpoints were tested using Postman.

## Author
Chethla Sai Teja
