from django.apps import AppConfig


class PressConfig(AppConfig):
    # Django 모델에서 자동 생성되는 기본 기본 키 필드의 유형을 지정
    default_auto_field = "django.db.models.BigAutoField"
    name = "press"
