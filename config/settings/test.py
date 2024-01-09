from .base import *  # NOSONAR
from .base import BASE_DIR

# CELERY
# ------------------------------------------------------------------------------
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#configuration
CELERY_BROKER_FAKE = True
BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {"NAME": "testdb.sqlite3"},
    }
}
