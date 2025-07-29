# Python 121 - Final Django Project

Welcome to your final project! This project will demonstrate your mastery of Python fundamentals from workshops 1-10 and Django web development concepts.

## 📋 Project Overview

Create a Django web application that incorporates all the concepts we've learned throughout the course. Choose one of the project options below and build a fully functional web application.

## 🎯 Project Options

### Option 1: Student Management System
Build a comprehensive student grade tracking system similar to our [`workshop_6/university.py`](workshop_6/university.py) examples.

**Core Features:**
- Student registration and profiles
- Course management
- Grade tracking and GPA calculation
- Teacher dashboard for grade entry
- Student dashboard for viewing grades

### Option 2: Personal Finance Tracker
Create a budgeting application using arithmetic concepts from [`workshop_2/arithmetic_operators.py`](workshop_2/arithmetic_operators.py).

**Core Features:**
- Income and expense tracking
- Category-based organization
- Monthly/yearly financial summaries
- Budget planning and alerts
- Transaction history

### Option 3: Library Management System
Expand on the concepts from [`django_project_1/store/models.py`](django_project_1/store/models.py).

**Core Features:**
- Book catalog management
- Member registration and profiles
- Book borrowing and return system
- Search functionality
- Inventory tracking

### Option 4: Recipe Sharing Platform
Build on list/dictionary concepts from workshops 5-6.

**Core Features:**
- Recipe creation and sharing
- Ingredient management
- Recipe search and filtering
- User ratings and reviews
- Meal planning tools

### Option 5: Event Management System
Create an event booking platform similar to the polls app structure.

**Core Features:**
- Event creation and management
- User registration for events
- Event calendar view
- Attendee management
- Event categories and filtering

## 🛠️ Technical Requirements

### 1. Project Structure
Follow the Django project structure from [django_project_1](django_project_1):
```
your_project/
├── manage.py
├── requirements.txt
├── your_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── your_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
├── templates/
│   ├── base.html
│   └── your_app/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── README.md
```

### 2. Python Concepts Integration

**Workshop 1-2: Fundamentals**
- Use proper variable naming from [`docs/workshop_1.md`](docs/workshop_1.md)
- Implement arithmetic operations where applicable
- Apply data types correctly

**Workshop 3-4: Control Flow**
- Use conditional statements in views and templates
- Implement loops for data display
- Handle user input validation

**Workshop 5-6: Data Structures**
- Use lists and dictionaries in your models
- Process collections of data
- Implement search and filtering

**Workshop 7-8: Functions and Classes**
- Create custom model methods
- Use class-based views (optional)
- Implement helper functions

**Workshop 9: File Operations**
- Handle file uploads (if applicable)
- Implement data export features
- Use file I/O like [`workshop_9/writing_to_file.py`](workshop_9/writing_to_file.py)

**Workshop 10: Modules and Web**
- Organize code into proper modules
- Apply web concepts from [`workshop_10/web.md`](workshop_10/web.md)
- Use virtual environment setup from [`workshop_10/project_1/README.md`](workshop_10/project_1/README.md)

### 3. Django Requirements

**Models (30 points)**
- Minimum 3 related models
- Proper field types and relationships
- Model methods and `__str__` representations
- Database migrations

**Views (25 points)**
- At least 5 different views
- Form handling with validation
- CRUD operations (Create, Read, Update, Delete)
- Error handling

**Templates (20 points)**
- Extend base template like [`django_project_1/templates/base.html`](django_project_1/templates/base.html)
- Dynamic content rendering
- Form templates
- Responsive design

**URLs (10 points)**
- Proper URL patterns
- App-level URL configuration
- Named URLs for easy maintenance

**Admin Interface (10 points)**
- Register all models
- Customize admin display
- Search and filtering capabilities

**Static Files (5 points)**
- CSS styling (build on [`django_project_1/static/style.css`](django_project_1/static/style.css))
- Responsive layout
- Clean, professional appearance

## 🚀 Getting Started

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.\.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate

# Install Django
pip install django

# Create requirements.txt
pip freeze > requirements.txt
```

### 2. Project Creation
```bash
# Create Django project
django-admin startproject your_project_name
cd your_project_name

# Create Django app
python manage.py startapp your_app_name

# Run initial migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 3. Development Workflow
1. **Plan your models** - Design your database schema
2. **Create models** - Define your data structure
3. **Make migrations** - `python manage.py makemigrations`
4. **Apply migrations** - `python manage.py migrate`
5. **Register admin** - Add models to admin interface
6. **Create views** - Implement your business logic
7. **Design templates** - Create your user interface
8. **Configure URLs** - Set up routing
9. **Add styling** - Implement CSS
10. **Test thoroughly** - Ensure everything works

## 🏆 Extra Challenges (Bonus Points)

### Performance Challenges
- Implement database query optimization
- Add pagination for large datasets
- Use Django's caching framework

### Feature Challenges
- Add user authentication and authorization
- Implement email notifications
- Create REST API endpoints
- Add search with autocomplete
- Implement data visualization charts

### Advanced Challenges
- Deploy to a cloud platform
- Add unit tests
- Implement real-time features with WebSockets
- Add internationalization (i18n)
- Create mobile-responsive PWA

## 📊 Evaluation Criteria

### Core Functionality (70%)
- **Models work correctly** (20%)
- **Views handle requests properly** (20%)
- **Templates render correctly** (15%)
- **Admin interface functional** (10%)
- **No critical bugs** (5%)

### Code Quality (20%)
- Clean, readable code
- Proper Python conventions
- Good use of workshop concepts
- Appropriate comments and documentation

### Extra Features (10%)
- Creative additions beyond requirements
- Advanced styling and UX
- Additional functionality
- Performance optimizations

## 📝 Submission Requirements

### Code Submission
- Complete Django project
- requirements.txt file
- README.md with setup instructions
- Database migrations included

### Documentation
- Project description and features
- Setup and installation instructions
- User guide with screenshots
- Technical challenges faced and solutions

### Demo Preparation
- 5-minute project demonstration
- Highlight key features
- Explain technical decisions
- Show code structure

## 💡 Tips for Success

1. **Start simple** - Get basic CRUD operations working first
2. **Use git** - Commit frequently with meaningful messages
3. **Test early** - Don't wait until the end to test features
4. **Ask questions** - Get help when stuck
5. **Plan your time** - Don't leave everything for the last week
6. **Focus on functionality** - Polish comes after core features work
7. **Document as you go** - Don't save documentation for the end

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Project Example](django_project_1)
- [Python Fundamentals](workshop_1) through [workshop_10](workshop_10)


Good luck with your final project! Remember, this is your chance to showcase everything you've learned and build something you can be proud of.

