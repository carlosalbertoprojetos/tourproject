release: python3 manage.py migrate
python manage.py collectstatic --noinput
web: gunicorn tourproject.wsgi --preload --log-file -