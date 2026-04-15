# Python Web App

This project contains two Django web services: `service1` and `service2`. Each service is in its own folder for separate Dockerization.

## Services

Each service has the following endpoints:
- `/health/`: Returns a JSON health check `{"status": "healthy"}`
- `/image/`: Serves the `me.jpg` image file from the service directory. If the file is not found, returns a 404 error.

## Setup

1. Ensure Python virtual environment is set up (`.venv` in the root).
2. Install dependencies: `pip install -r service1/requirements.txt` (same for service2).
3. Add `me.jpg` image file to each service folder.
4. Run the service: `cd service1; python manage.py runserver` (default port 8000).

## Docker and Kubernetes

Write separate Dockerfiles in each service folder. Use Kubernetes manifests to deploy both services.

## Troubleshooting

- If image not found, ensure `me.jpg` is in the correct directory.
- Django errors: Run `python manage.py check` to validate.