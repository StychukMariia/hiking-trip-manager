# Hiking Trip Manager

A Django-based web application for managing hiking expeditions, hikers, and regions. 

## Features
- **Backend:** Built with Django, utilizing Class-Based Views and customized ORM queries.
- **Authentication:** Custom User model (`Hiker`) with secure login/logout functionality.
- **Frontend:** Fully responsive custom UI using Bootstrap 5 (Bootswatch 'Darkly' theme).
- **Data Management:** Full CRUD operations, search functionality, and pagination.

**1. Setup environment and install dependencies:**
```bash
git clone [https://github.com/StychukMariia/hiking_trip_manager.git](https://github.com/StychukMariia/hiking_trip_manager.git)
cd hiking_trip_manager
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**2. Configure Environment Variables:**
Create a `.env` file in the root directory by copying `.env.sample`:
```bash
cp .env.sample .env  # On Windows PowerShell: copy .env.sample .env
