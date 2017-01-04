"""
WSGI config for worldofsoka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/ubuntu/worldofsoka.com/worldofsoka')
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

os.environ["DJANGO_SETTINGS_MODULE"] = "worldofsoka.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
