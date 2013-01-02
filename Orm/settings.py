DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db1175101-test',                      # Or path to database file if using sqlite3.
        'USER': 'db1175101-test',                      # Not used with sqlite3.
        'PASSWORD': 'test322794',                  # Not used with sqlite3.
        'HOST': 'wp197.webpack.hosteurope.de',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',          # Set to empty string for default. Not used with sqlite3.
    }
}


DATABASE_OPTIONS = {
    "timeout": 5,
}



INSTALLED_APPS = (
    'db',
    'south', 
    )
    

TEMPLATE_DIRS=(
    '',
    )
