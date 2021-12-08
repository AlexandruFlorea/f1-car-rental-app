from .base import *
import os


if os.environ.get("DJANGO_SETTINGS_MODULE") == 'f1experience.settings.prod':
    from .prod import *
else:
    from .dev import *
