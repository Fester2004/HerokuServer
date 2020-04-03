from urllib.parse import urlparse
from HerokuServer.settings import *


MIDDLEWARE = \
    ['whitenoise.middleware.WhiteNoiseMiddleware'] + \
    MIDDLEWARE

# DEBUG = False
ALLOWED_HOSTS = ['djangodimon.herokuapp.com']

db_url = urlparse(os.environ.get('DATABASE_URL'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': db_url.hostname,
        'PORT': db_url.port,
        'USER': db_url.username,
        'PASSWORD': db_url.password,
        'NAME': db_url.path[1:],
    },
}