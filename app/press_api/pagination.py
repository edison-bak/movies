from rest_framework.pagination import PageNumberPagination


# api 페이지 20페이지 한계로 설정
class PostPageNumberPagination(PageNumberPagination):
    page_size = 20
