Here’s an **industry-standard** documentation template that is clear, professional, and provides all necessary details for setting up and running the application for your assignment.

---

# B_Store Project Documentation

## Overview

B_Store is a Django-based book management system that includes both traditional web views and API endpoints for managing books. It also implements user authentication using JSON Web Tokens (JWT) to secure certain operations like creating, updating, and deleting books. 

This document provides a step-by-step guide to set up, run, and test the application in a development environment.

---

## 1. Prerequisites

Ensure the following software is installed on your system:

- **Python 3.x** (Python 3.8 or higher recommended)
- **pip** (Python package installer)
- **MySQL** (Database)
- **Virtualenv** (Recommended for Python dependency management)
- **Django 5.1** or higher
- **Django REST Framework** (For building API endpoints)
- **djangorestframework_simplejwt** (For JWT authentication)

### Required Python Packages

- Django
- djangorestframework
- djangorestframework_simplejwt
- MySQL client

---

## 2. Project Setup

### Step 1: Clone the Project

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-repo/B_Store.git
cd B_Store
```

### Step 2: Create a Virtual Environment

It is recommended to create and activate a virtual environment to manage project dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# For Linux/macOS:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt` file, install the core dependencies manually:

```bash
pip install django djangorestframework mysqlclient djangorestframework_simplejwt
```

### Step 4: Database Setup

The project uses **MySQL** as its database. You need to set up a MySQL database with the following credentials:

- **Database Name**: `BSDB`
- **Username**: `root`
- **Password**: `pass@123`

Run the following command in MySQL to create the database:

```sql
CREATE DATABASE BSDB;
```

### Step 5: Configure Database in Django

Open the `settings.py` file and make sure the database configuration matches the MySQL setup:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "BSDB",
        "USER": "root",
        "PASSWORD": "pass@123",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### Step 6: Run Database Migrations

Apply the migrations to create the necessary tables in the database:

```bash
python manage.py migrate
```

### Step 7: Create Superuser

Create a superuser for accessing the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

---

## 3. Running the Application

### Step 1: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

### Step 2: Admin Access

You can access the Django admin interface at `http://127.0.0.1:8000/admin` by logging in with the superuser credentials you created earlier.

---

## 4. API Endpoints

This application includes several API endpoints built using Django REST Framework. The following endpoints are available for managing books:

### Public Endpoints:
- **GET** `/api/books/`: List all books.
- **GET** `/api/books/{id}/`: Retrieve a specific book by ID.

### Protected Endpoints (Require JWT authentication):
- **POST** `/api/books/`: Create a new book.
- **PUT** `/api/books/{id}/`: Update an existing book.
- **DELETE** `/api/books/{id}/`: Delete a book.

### JWT Authentication Endpoints:
- **POST** `/api/register/`: Register a new user.
- **POST** `/api/login/`: Log in and obtain a JWT token.

### Usage:

For operations that require authentication, include the JWT token in the request headers:

```http
Authorization: Bearer <your-token>
```

---

## 5. JWT Authentication Setup

The application uses **JWT (JSON Web Token)** authentication. Follow these steps to use it:

1. **User Registration** (`/api/register/`): Register a new user.
2. **User Login** (`/api/login/`): Obtain a JWT token.

The JWT token is required to access protected endpoints (POST, PUT, DELETE).

---

## 6. Static and Media Files

### Static Files:
Static files such as CSS and JavaScript are served from the `static/` directory. To collect and prepare static files, run:

```bash
python manage.py collectstatic
```

### Media Files:
Uploaded files, such as book images, are stored in the `media/` directory. Make sure the `MEDIA_ROOT` and `MEDIA_URL` settings are correctly configured in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 7. Testing

To run the test suite for the application, use the following command:

```bash
python manage.py test
```

This will run all unit tests, including those for the book model and other functionality.

---

## 8. Deployment Considerations

- Set `DEBUG = False` in production.
- Set up a proper environment variable for the `SECRET_KEY`.
- Configure allowed hosts by setting the `ALLOWED_HOSTS` variable in `settings.py`.
- Ensure proper static and media file handling for deployment.

---

## 9. Project Structure

The structure of the project is as follows:

```
B_Store/
│
├── B_Store/                # Main project settings and configuration files
│   ├── settings.py
│   └── urls.py
│
├── api/                    # API endpoints and logic
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── blog/                   # Traditional views, models, and templates
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── static/                 # Static files (CSS, JavaScript)
│
├── media/                  # Media uploads (e.g., book images)
│
├── templates/              # HTML templates
│   ├── book_list.html
│   ├── book_form.html
│   ├── book_confirm_delete.html
│   └── registration/
│
├── manage.py               # Django management script
└── requirements.txt        # Python package dependencies
```

---

With this documentation, the **B_Store** application should be easy to set up, run, and extend. If you are deploying this to production, be sure to configure the necessary security settings (such as `ALLOWED_HOSTS`, `DEBUG`, and `SECRET_KEY`) appropriately.
