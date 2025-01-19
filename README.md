Gas Utility Customer Service Portal 🏭
A Django-based portal for managing gas utility service requests and customer support.

🌟 Features
For Customers:
Submit and track service requests
View request history and updates
Manage profiles and upload documents

For Support:
Manage and update tickets
Assign staff and track status
Add comments and resolve requests

User Management:
Secure login and password recovery
Role-based access


🛠️ Tech Stack
Backend: Python, Django
Database: MySQL
Frontend: HTML, CSS, JavaScript

📦 Setup
- Clone the repo:
- https://github.com/Karan-8418-Dev/gas-utility-customer-service.git
- cd gas-utility-customer-service
- Set up virtual environment:
- python -m venv venv
- source venv/bin/activate  # Linux/Mac
- venv\Scripts\activate     # Windows

Install dependencies:
pip install -r requirements.txt
Configure .env:
cp .env.example .env
# Update with your settings/#You Can Directly Add Configurations In Project Settings
Run migrations:
python manage.py makemigrations
python manage.py migrate

Create a superuser:
python manage.py createsuperuser
Start the server:
python manage.py runserver

🏗️ Folder Structure
gas_utility/
 - accounts/         # User authentication
 - customer_portal/  # Customer features
 - customer_support/ # Support dashboard
 - static/           # CSS, JS, images
 - templates/        # HTML templates
 - media/            # Uploaded files

🔐 Environment Variables
DEBUG=True/False
SECRET_KEY=your-secret-key
DB_NAME=your_database_name

🚀 Usage
Admin: http://localhost:8000/admin/
# same login api endpoint  just enter your credentials as per that you will be redirected to your dashboard
Customer Portal: http://127.0.0.1:8000/login/
<!-- Support Dashboard: http://localhost:8000/support/ -->

🧪 Testing
Run tests:
python manage.py test