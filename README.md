# Slate Backend API

## Project Overview

Slate Backend API is a Django-based application that provides a role-based authentication system for schools, parents, and students. It allows users to register, login, manage student achievements, and access role-specific dashboards.

## Features

- User registration and authentication
- Role-based access control (School, Parent, Student)
- JWT-based authentication
- Password reset functionality
- Student achievement management
- Role-specific dashboards

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/prajwalsuryawanshi/slate_backend_assignment.git
   cd slate_backend_assignment
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- POST `/auth/register/`: Register a new user
- POST `/auth/login/`: Login and obtain JWT token
- POST `/auth/forgot-password/`: Reset user password
- GET `/student/achievements/<student_id>/`: Retrieve student achievements
- GET `/parent-dashboard/`: Access parent dashboard
- GET `/school-dashboard/`: Access school dashboard
- GET `/student-dashboard/`: Access student dashboard

## Testing

You can use the provided Postman collection (`Slate-Backend-API.postman_collection.json`) to test the API endpoints. Import this collection into Postman to get started.
