# Dente Care
`Site for dental clinic` <br />
https://dente-clinic.herokuapp.com/

Build by using Django 3 and Python 3

# deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Connect your PostgreSQL db in file dente/settings.py

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}`

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Load all data from JSON files to db by using next commands:

`python3 manage.py loaddata aboutus.json`
`python3 manage.py loaddata feedback.json`
`python3 manage.py loaddata news.json`
`python3 manage.py loaddata pricing.json`

5 - Run app:

`python3 manage.py runserver`
