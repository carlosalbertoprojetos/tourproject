release: python manage.py migrate
web: gunicorn tourproject.wsgi --preload --log-file -
python3
manage.py collectstatic --noinputpip install gunicorn