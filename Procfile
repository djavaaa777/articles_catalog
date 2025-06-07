web: gunicorn articles_catalog.wsgi:application
release: python manage.py migrate && python manage.py loaddata data.json && python manage.py collectstatic --noinput && python manage.py create_admin
