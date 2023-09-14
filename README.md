# Capstone - Django Music Group Web Application

Welcome to the Capstone repository, a Django-based web application for managing a musical group.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Using a Virtual Environment (venv)](#using-a-virtual-environment-venv)
  - [Using Docker](#using-docker)
- [Running the Application](#running-the-application)
- [Accessing the Application](#accessing-the-application)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can run this application, you'll need the following prerequisites:

- Python 3.11
- Django (specified in `requirements.txt`)
- Docker (optional, for containerized deployment)

## Getting Started

### Using a Virtual Environment (venv)

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Myworld234/capstone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd capstone
   ```

3. Create a virtual environment (venv):

   ```bash
   python -m virtualenv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Using Docker

1. Clone the repository to your local machine:

   ```bash
   git clone https://hub.docker.com/r/tobby247/capstone
   ```

2. Navigate to the project directory:

   ```bash
   cd capstone
   ```

3. Build a Docker image:

   ```bash
   docker build -t capstone .
   ```

## Running the Application

### Using a Virtual Environment (venv)

1. Apply Django migrations:

   ```bash
   python manage.py migrate
   ```

2. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

### Using Docker

1. Run the Docker container (map port 8000 as needed):

   ```bash
   docker run -p 8000:8000 capstone
   ```

## Accessing the Application

Once the application is running:

- Access the application in your web browser at [http://localhost:8000](http://localhost:8000)
