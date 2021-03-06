"""
WSGI config for paw_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paw_project.settings")
# add project to path
import sys

sys.path.append('/home/paxson/web_dev/paw_project/paw_project')

# add virtualenv site-packages to path
sys.path.append('/home/paxson/.virtualenvs/paw_project/lib/python3.3/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"] = "paw_project.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
