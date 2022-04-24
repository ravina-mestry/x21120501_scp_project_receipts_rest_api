This is a Python Django framework project.

It requires python3, MySQL and RabbitMQ installed on the machine.
Follow the below steps to run it locally.

1. git clone master branch.
git clone https://github.com/ravina-mestry/x21120501_scp_project_receipts_rest_api.git

2. Update below sections in receipts_rest_api/settings.py
- Enable Debug on local machine.
DEBUG = True

- MySQL DB Configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': '<mysql_user_name>',
        'PASSWORD': '<mysql_user_password>',
        'HOST': '<hostname>',
        'PORT': '3306',
    }
}

- Email SMTP Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_USE_TLS = 
EMAIL_PORT = 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

- Celery Broker
CELERY_BROKER_URL = '<rabbit mq url amqp://<username>:<password>@<hostname>>'

3. Create virtual environment.
cd x21120501_scp_project_receipts_rest_api

python -m venv receipts_rest_api_venv
source receipts_rest_api_venv/bin/activate

pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

4. Populate database
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

5. Run local server
python manage.py runserver 8080

6. Run Celery worker in a separate console with virtual environment enabled.
source receipts_rest_api_venv/bin/activate
celery -A receipts_rest_api worker --pool=solo -l info

7. Generate API token
python manage.py drf_create_token <username>
