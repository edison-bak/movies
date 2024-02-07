from django.apps import AppConfig


class PressApiConfig(AppConfig):
    # 어플리케이션 내에서 새로 생성되는 모든 모델의 기본 자동 증가 필드는 BigAutoField로 생성
    default_auto_field = "django.db.models.BigAutoField"
    name = "press_api"
