# Excel to MySQL Django API with JWT Authentication

Automated workflow for importing Excel data into MySQL and providing secure API access with JWT authentication.

## Features

- Excel to MySQL data import
- JWT authentication
- Profile filtering by department, designation, and name
- Data validation
- RESTful API

## Prerequisites

- Python 3.8+
- MySQL 5.7+
- Django project with app created
- MySQL database created (e.g., `sybrant`)

## Libraries Used

**Data Processing:**
- pandas
- openpyxl

**Database:**
- SQLAlchemy
- PyMySQL

**API Framework:**
- Django
- djangorestframework
- djangorestframework-simplejwt

## Database Table Structure

**Table:** `person_profiles`

   Query_path => sybrant\raw_insert\raw.sql
   
## API Endpoints

### Authentication

**Obtain Token:**
- **URL:** `/api/token/`
- **Method:** POST
- **Request:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
- **Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

**Refresh Token:**
- **URL:** `/api/token/refresh/`
- **Method:** POST
- **Request:**
```json
{
  "refresh": "<refresh_token>"
}
```
- **Response:**
```json
{
  "access": "<new_access_token>"
}
```

### Profile Endpoints

**Get All Profiles:**
- **URL:** `/api/profiles/`
- **Method:** GET
- **Authorization:** Bearer Token
- **Response:**
```json
{
    "status": 200,
    "total": 111,
    "limit": 1,
    "offset": 0,
    "data": [
        {
            "id": "SYB26",
            "name": "Abraham E.",
            "email": "abe@datacy.com",
            "phone": "+1 408-647-4412",
            "designation": "Chief Technology Officer",
            "department": "C-Suite, Engineering & Technical"
        }
    ]
}
```

**Filter Profiles:**
- **URL:** `/api/profiles/?department=IT&designation=Manager`
- **Method:** GET
- **Authorization:** Bearer Token
- **Query Parameters:**
  - `id` (optional)
  - `department` (optional)
  - `designation` (optional)
- **Response:** Same as above, filtered

## Excel Import Process

**Required Excel Columns:**
- id
- name
- email
- phone
- designation
- department

**Process Steps:**
1. Load Excel file using pandas
2. Validate email addresses
3. Clean and standardize phone numbers
4. Connect to MySQL database using SQLAlchemy
5. Insert records into person_profiles table
6. Handle duplicates and constraint errors
7. Log errors and display statistics

## Installation Steps

1. Clone repository
2. Create virtual environment
3. Install dependencies from requirements.txt
4. Configure database credentials
5. Run Django migrations
6. Create superuser
7. Configure JWT settings in Django settings.py
8. Run import script for Excel data
9. Start Django development server

## Error Handling

**HTTP Status Codes:**
- 200: Success
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Server Error

**Common Errors:**
- Invalid credentials
- Expired token
- Missing authorization header
- Database connection errors
- Duplicate email addresses
- Invalid data format

## Project Structure
 - Folder => raw_insert (Excel to Db)
 - Folder => Demo (API development)
   -  projectname => demo
   -  appname => sybrantapi
