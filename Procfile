web: gunicorn tourproject.wsgi --preload --log-file -
python3
manage.py collectstatic --noinput
release: python3 manage.py migrate
