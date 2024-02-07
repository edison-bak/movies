from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # "/admin/" 경로로 접근 시, 관리자 페이지로 연결
    path("admin/", admin.site.urls),
    # "/press/" 경로로 시작하는 요청은 "press.urls"에서 정의한 URL 패턴으로 연결
    path("press/", include("press.urls")),
    # "/press_api/" 경로로 시작하는 요청은 "press_api.urls"에서 정의한 URL 패턴으로 연결
    path("press_api/", include("press_api.urls")),
]
