release: python manage.py migrate
web: gunicorn config.wsgi:application
worker_beat: celery --app=config.celery_app worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --concurrency 2
