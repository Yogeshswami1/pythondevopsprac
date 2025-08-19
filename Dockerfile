# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Gunicorn server
CMD ["gunicorn", "notes_project.wsgi:application", "--bind", "0.0.0.0:8000"]
