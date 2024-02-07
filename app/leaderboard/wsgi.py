"""
WSGI config for leaderboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/

wsgi.py 파일은 Django 웹 어플리케이션을 WSGI (Web Server Gateway Interface)
서버에 연결하기 위한 파일입니다. WSGI는 Python 언어로 작성된 웹 어플리케이션과
웹 서버 간의 표준 인터페이스를 제공합니다. 

보통 웹 서버 (예: Apache, Nginx)가 WSGI를 지원하는 경우, wsgi.py 파일을 통해
Django 어플리케이션을 서버와 통합하여 안정적인 웹 애플리케이션을 제공할 수 
있습니다.

1. 웹서버는 요청이 있을 경우 정보와 콜백함수를 WSGI에 전달. 
2. 전달된 정보를 해석해 장고 웹 어플로 전달한다.
3. 장고 웹 어플은 파이썬 스크립트를 이용해 정보를 처리하고 끝낸 결과를 WSGI
에 다시 전달.
4. 이 정보를 콜백함수를 이용해 웹서버에 다시 전달.
이렇듯 서버, WSGI, 장고 웹 어플이 상호작용하며 동작한다.
"""

import os

from django.core.wsgi import get_wsgi_application

# DJANGO_SETTINGS_MODULE 환경 변수가 설정되지 않은 경우, 기본값으로 "leaderboard.settings"를 사용
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaderboard.settings")

# Django 웹 어플리케이션을 WSGI 서버와 연결
application = get_wsgi_application()
