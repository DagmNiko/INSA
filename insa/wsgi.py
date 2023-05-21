"""
WSGI config for insa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/insa')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insa.settings')
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent

# load_dotenv(os.path.join(BASE_DIR / 'insa', '.env'))
application = get_wsgi_application()
