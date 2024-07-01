# BitTechnologies-Website
This repository contains the test done by juan pablo perez santos for the company bittechnologies which has the creation of a CRUD API for properties and leases, and its respective graphical interface using Django templates.

## Requirements

Make sure you have the following requirements installed before you begin:

- PostgreSQL 14.5
- Python 3.10.6
- Docker 26.1.4

## Initial configuration

### Clone the Repository

```
git clone <repository-url>
cd property_management
```

Running with enviroment local
To run the project using enviroment local, follow these steps:

Create a database named property_db.

Set the user and password in property_management/settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'property_db',
        'USER': 'your_user',  # Change according to your local configuration
        'PASSWORD': 'your_password',  # Change according to your local configuration
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Virtual environment configuration (optional but recommended) WINDOWS:
```
python -m venv env
env\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Apply migrations
```
python manage.py migrate
```

----------------------------------------------------

Running with Docker Compose, to run the project using Docker Compose, follow these steps:

Build and Start Containers:

```
docker-compose up --build
```

This command will build the necessary images and start the containers as defined in docker-compose.yml.

Access the Application

Once all containers are up and running, the application will be available at http://localhost:8000/.


