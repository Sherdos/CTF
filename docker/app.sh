#!/bin/bash

# Применяем миграции
python manage.py makemigrations
python manage.py migrate

# Создаем суперпользователя
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "admin"
email = "admin@example.com"
password = "admin"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Суперпользователь создан!")
else:
    print("Суперпользователь уже существует.")
EOF

# Запускаем сервер
python manage.py runserver 0.0.0.0:8000