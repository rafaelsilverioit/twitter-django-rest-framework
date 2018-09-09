from rest_framework.pagination import PageNumberPagination


class APIPagination(PageNumberPagination):
    max_page_size = 500
    page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'size'
