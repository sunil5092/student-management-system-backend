# Student Management System – Backend

## Live Demo
Swagger API Documentation:  
https://student-management-system-backend-ttkh.onrender.com/docs


## Overview
A backend REST API built using FastAPI and PostgreSQL to manage student records.  
The system supports full CRUD operations with pagination, filtering, and clean service-layer architecture.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## Features
- Create, read, update, and delete student records
- Pagination and filtering for large datasets
- Service-layer architecture for clean separation of concerns
- Interactive API documentation using Swagger

## API Endpoints
- POST /students – Create a new student
- GET /students – Get all students (supports pagination & filtering)
- GET /students/{id} – Get student by ID
- PUT /students/{id} – Update student details
- DELETE /students/{id} – Delete a student

## How to Run Locally
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies from requirements.txt
4. Configure PostgreSQL connection
5. Run the FastAPI server using uvicorn

## What I Learned
- Designing RESTful APIs using FastAPI
- Database modeling with SQLAlchemy and PostgreSQL
- Implementing full CRUD operations
- Pagination, filtering, and clean backend architecture
- Debugging real-world backend issues

## Future Enhancements
- JWT-based authentication and authorization
- Role-based access (Admin / Student)
- Dockerization and deployment
>>>>>>> 3f1527534b939b5c9042d02cbdd2e77dd4126374

