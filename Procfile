release: py manage.py migrate
web: gunicorn tourproject.wsgi --preload --log-file -
python manage.py collectstatic --noinput