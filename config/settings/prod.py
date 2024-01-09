from .base import *  # NOSONAR

AUTH_COOKIE_SECURE = True
AUTH_COOKIE_HTTP_ONLY = True

CELERY_BROKER_URL = "pyamqp://guest@localhost//"
CELERY_RESULT_BACKEND = "redis://localhost"
