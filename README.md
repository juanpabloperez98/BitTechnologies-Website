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

1) create a database in your local postgres with the name of your choice

2) Virtual environment configuration (optional but recommended) WINDOWS:
```
python -m venv env
env\Scripts\activate
```
3) Install dependencies:
```
pip install -r requirements.txt
```
4) Copy the .env file provided by the project developer (Juan Pablo Perez) to the level of the manage.py file. It contains the environment variables.
The structure would be
```
DATABASE_NAME=<database_name>
DATABASE_USER=<database_user>
DATABASE_PASSWORD=<database_password>
DATABASE_HOST=<database_host>
DATABASE_PORT=<database_port>
DEBUG=<1 or 0>
DJANGO_SETTINGS_MODULE=property_management.settings
IS_DOCKER=<bool is run with docker>
```

5) Apply migrations
```
python manage.py migrate
```

----------------------------------------------------

Running with Docker Compose, to run the project using Docker Compose, follow these steps:

1) Copy the .env file provided by the project developer (Juan Pablo Perez) to the level of the manage.py file. It contains the environment variables.
The structure would be
```
DATABASE_NAME=<database_name>
DATABASE_USER=<database_user>
DATABASE_PASSWORD=<database_password>
DATABASE_HOST=<database_host>
DATABASE_PORT=<database_port>
DEBUG=<1 or 0>
DJANGO_SETTINGS_MODULE=property_management.settings
IS_DOCKER=<bool is run with docker>
```
2) Build and Start Containers:

```
docker-compose up --build
```

This command will build the necessary images and start the containers as defined in docker-compose.yml.

Access the Application

Once all containers are up and running, the application will be available at http://localhost:8000/.

## Postman Collection

The BitTechnologies-Website.postman_collection.json file contains the examples in postman to import and test the API.


