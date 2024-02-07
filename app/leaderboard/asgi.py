"""
ASGI config for leaderboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# DJANGO_SETTINGS_MODULE 환경 변수 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaderboard.settings")

# ASGI 응용 프로그램 얻기
application = get_asgi_application()
