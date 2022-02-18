web: gunicorn tourproject.wsgi --preload --log-file -
python3 manage.py migrate
release: python3 manage.py migrate
python3 manage.py collectstatic --noinput