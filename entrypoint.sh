#!/bin/sh


echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@email.com", "admin123")
    print("Superuser created")
else:
    print("Superuser already exists")
END

echo "Starting server..."
exec "$@"