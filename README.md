# Student Management System – Backend

## Overview
A backend REST API built with FastAPI and PostgreSQL to manage student records, with JWT authentication.
The system supports full CRUD operations with pagination, name filtering, and a clean service-layer architecture.

**Deployment:** being moved to a new host — the live API docs link will be updated here when the redeploy is verified.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT authentication (python-jose) with bcrypt password hashing (passlib)

## Features
- User registration and login with JWT bearer tokens (`/auth/register`, `/auth/login`)
- All student endpoints require a valid token
- Create, read, update, and delete student records
- Paginated student list with total count (`{total, items}`) and case-insensitive name filtering
- Duplicate email returns HTTP 409 instead of a server error
- Service-layer architecture for clean separation of concerns
- Interactive API documentation using Swagger (`/docs`)

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | /auth/register | Register a new user |
| POST | /auth/login | Log in and receive a JWT access token |
| POST | /students | Create a new student |
| GET | /students | List students (pagination: `skip`, `limit`; filter: `name`) |
| GET | /students/{id} | Get a student by ID (404 if not found) |
| PUT | /students/{id} | Update student details (partial updates supported) |
| DELETE | /students/{id} | Delete a student |

## How to Run Locally
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies from requirements.txt
4. Set environment variables: `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM` (e.g. `HS256`), `ACCESS_TOKEN_EXPIRE_MINUTES`
5. Run the FastAPI server using uvicorn: `uvicorn app.main:app --reload`
6. Open http://localhost:8000/docs and use the Authorize button with a token from `/auth/login`

## What I Learned
- Designing RESTful APIs using FastAPI
- Database modeling with SQLAlchemy and PostgreSQL
- Implementing JWT authentication: password hashing, token creation, and route protection via dependencies
- Implementing full CRUD operations, pagination, and filtering
- Debugging real backend issues — including a duplicated route definition that silently shadowed the paginated list endpoint

## Future Enhancements
- Role-based access (Admin / Student)
- Refresh tokens
- Automated test suite
