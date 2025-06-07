web: gunicorn articles_catalog.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py create_admin
