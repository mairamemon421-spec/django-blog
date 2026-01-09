Django Blog Application

A production-ready, multi-app blog application built with Django, featuring role-based access control, draft and publish workflows, image uploads, category management, and a conditional commenting system.
The project follows real-world Django practices and is deployed live on PythonAnywhere.

🌐 Live Demo
👉 https://mairadev.pythonanywhere.com/


Overview

This project is a multi-user blogging platform built using Django’s default authentication system and permission framework.
It uses Django Groups, Permissions, and staff-based access control to manage different roles within the system.

The application supports complete blog lifecycle management, including drafts, published posts, images, categories, comments, and a custom-designed frontend using Bootstrap.


---

Key Features

Django default User authentication

Group-based role management (Admin, Manager, Editor, User)

Staff-only access to dashboards and management views

Create, edit, delete, and manage blog posts

Draft and published post status

Image upload support for posts

Category CRUD functionality

Comment system with authentication checks

keywork search

Bootstrap-based responsive UI

Custom 404 error page

Django Admin integration

Static and media file handling

Deployed on PythonAnywhere


Roles & Permissions:

The project uses Django Groups + Permissions combined with is_staff checks.

Super Admin (Superuser)

Full access to Django Admin Panel

Manage users, groups, and permissions

Manage categories and blog posts

Manage dashboards and site-level settings (e.g. social links)



---

Manager

Manage users

Create, edit, and delete blog posts

Create, edit, and delete categories

Access staff dashboards



---

Editor

Create, edit, and delete blog posts

Create and manage categories

No access to user management

Staff-only access


This permission structure ensures secure access, scalability, and clear responsibility separation.


Comment System

All visitors can view comments

Only authenticated users can post comments

Guest users are restricted from commenting


Frontend & UI

Django Templates

Bootstrap for layout and responsiveness

Custom-designed 404 error page

HTML, CSS, and light JavaScript usage



---

Technology Stack

Python

Django

HTML5 / CSS3

Bootstrap

JavaScript

SQLite3

PythonAnywhere



---



Project Structure

blog/
├── blog_main/              # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blogs/                  # Blog & comment functionality
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── context_processors.py
│   └── migrations/
│
├── dashboards/             # Staff dashboards & management
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── migrations/
│
├── pages/                  # Static & informational pages
│
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── media/                  # Uploaded blog images
│
├── env/                    # Virtual environment
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md


---

Deployment

The application is deployed on PythonAnywhere and is publicly accessible.

🔗 Live URL:(https://mairadev.pythonanywhere.com/)

Static and media files are properly configured for production use.


Why This Project

This project goes beyond a basic Django blog by implementing:

Group-based permission handling

Staff-only dashboards

Draft and published content workflow

Conditional commenting system

Real deployment on a production server


It is designed to reflect real-world Django backend development.


Future Enhancements

Pagination

Advanced search and filtering

Rich text editor for posts

User profile pages

API integration



License

This project is licensed under the MIT License.



Author

Developed by Maira Memon
Django Developer | Python Enthusiast
