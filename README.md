# CampusConnect

CampusConnect is a Django-based student event management web application. It allows students to create and manage events, browse events created by other users, register for events, and manage their registered events through a personal dashboard.

The application uses **Django 6.1**, **PostgreSQL**, **Bootstrap**, and **JavaScript** to provide a responsive and user-friendly experience.

---

## Features

### User Accounts

* User registration
* User login and logout
* Email verification during registration
* Secure password handling using Django's built-in authentication system
* User-specific dashboard

### Event Management

Users can:

* Create new events
* View event details
* Edit events they created
* Delete events they created
* Add event descriptions
* Set an event date
* Add an event location
* Select event categories
* Prevent events from being created with invalid/past dates

### Event Registration

Users can:

* Browse available events
* Register for events
* View events they have registered for
* Cancel their event registration
* View event details

### Dashboard

The dashboard allows users to see:

* Events they have created
* Events they have registered for
* Event dates
* Event locations
* Event descriptions
* Links to view individual event details

The dashboard uses a responsive card layout so that events are displayed side-by-side and automatically wrap onto additional rows when required.

### User Interface

* Responsive Bootstrap navigation
* Responsive event cards
* Bootstrap buttons and components
* JavaScript interactions
* User-friendly forms
* Consistent CampusConnect styling
* Favicon included

---

## Technologies Used

### Backend

* Python
* Django 6.1
* PostgreSQL

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Database

* PostgreSQL

### Email

* MailerSend SMTP
* Django email functionality

### Deployment

* Render

---

## Project Structure

```text
CampusConnect/
│
├── campusconnect/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── events/
│   ├── migrations/
│   ├── templates/
│   │   └── events/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── event_detail.html
│   │       ├── event_form.html
│   │       ├── event_list.html
│   │       └── ...
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jmichael2025/Framework.git
```

Navigate into the project:

```bash
cd Framework
```

---

### 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

If PowerShell prevents activation, the following can also be used:

```powershell
.venv\Scripts\activate.bat
```

---

### 3. Install Dependencies

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

The project uses Django, PostgreSQL support, Pillow, python-dotenv and the other packages listed in `requirements.txt`.

---

## PostgreSQL Database Setup

CampusConnect uses PostgreSQL rather than the default SQLite database.

Create a PostgreSQL database for the project, for example:

```text
campusconnect_db
```

Configure the database connection through environment variables.

The application uses the following database variables:

```text
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

For a local PostgreSQL installation, these values should match the PostgreSQL database and user configured on the development machine.

---

## Environment Variables

Sensitive configuration is stored in environment variables rather than being committed to GitHub.

Create a `.env` file in the project directory.

Example:

```text
DB_NAME=campusconnect_db
DB_USER=postgres
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5433

EMAIL_HOST=your_email_host
EMAIL_PORT=587
EMAIL_HOST_USER=your_email_username
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_email_address
```

**Do not commit the `.env` file to GitHub.**

The `.env` file should be included in `.gitignore`.

---

## Database Migrations

After configuring PostgreSQL, run:

```powershell
python manage.py makemigrations
```

Then:

```powershell
python manage.py migrate
```

---

## Create an Administrator Account

To create a Django administrator account:

```powershell
python manage.py createsuperuser
```

Follow the instructions in the terminal.

The Django admin area can then be accessed through:

```text
/admin/
```

---

## Run the Development Server

Start the Django development server:

```powershell
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

---

# Testing the Application

To fully test CampusConnect, an evaluator should create a user account and test the main features of the application.

## 1. Register an Account

Create a new account using the registration page.

Test:

* Username
* Email address
* Password
* Password confirmation
* Email verification

Complete the email verification process before logging in.

---

## 2. Login

Log in using the newly created account.

Verify that:

* Login succeeds with valid credentials
* Invalid credentials are rejected
* The user can access their dashboard after logging in

---

## 3. Create an Event

From the application, create a new event.

Test:

* Event title
* Description
* Date
* Location
* Category

After creating the event, confirm that it appears in **My Created Events** on the dashboard.

---

## 4. View Event Details

Open the event using **View Details**.

Check that the event information is displayed correctly.

---

## 5. Edit an Event

Open an event created by the logged-in user and test the edit functionality.

Change one or more event details and confirm that the changes are saved.

---

## 6. Delete an Event

Delete an event created by the user.

Confirm that the event is removed from the user's created events.

---

## 7. Browse Events

Open the event listing page and confirm that available events are displayed.

Check that users can view event information and access individual event details.

---

## 8. Register for an Event

Register for an event created by another user.

Confirm that the event appears under:

```text
My Registered Events
```

on the dashboard.

---

## 9. Cancel Event Registration

Cancel registration for an event.

Confirm that the event is removed from the user's registered events.

---

## 10. Dashboard

Check that the dashboard correctly displays:

* Welcome message
* Created events
* Registered events
* Event descriptions
* Dates
* Locations
* View Details buttons

The event cards should be displayed side-by-side on larger screens and automatically wrap when additional events are added.

---

## 11. Navigation

Test the main navigation links and buttons.

Check:

* Home
* Events
* Dashboard
* Create Event
* Login
* Logout
* Other available navigation options

---

## 12. Responsive Design

Test the application at different browser window sizes.

Confirm that:

* Navigation remains usable
* Event cards resize correctly
* Multiple events wrap onto additional rows
* Buttons remain accessible
* Text remains readable

---

# Email Verification

CampusConnect uses **MailerSend SMTP** for email verification.

When a new user registers, the application sends a verification email.

The user must verify their email address before accessing the appropriate authenticated functionality.

Email configuration is controlled through environment variables and should not be stored directly in the source code.

---

# Deployment

The application can be deployed using Render.

The deployed application requires the necessary environment variables to be configured in the Render service.

Database variables:

```text
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

Email variables:

```text
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL
```

The production database should be a PostgreSQL database hosted for the deployed application.

---

# Security

The project follows Django's standard security practices, including:

* Django authentication
* Password hashing
* CSRF protection
* Environment variables for sensitive configuration
* `.env` excluded from Git
* User-specific access to event management functionality

Sensitive credentials such as database passwords, email passwords, and secret keys should never be committed to the repository.

---

# Requirements

The project dependencies are stored in:

```text
requirements.txt
```

To install them:

```powershell
pip install -r requirements.txt
```

---

# Author

**Jasmin Michael**

CampusConnect was developed as a Django framework project demonstrating database integration, user authentication, event management, PostgreSQL, responsive Bootstrap design, and JavaScript functionality.
