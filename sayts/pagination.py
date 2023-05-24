from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = '1'
    max_page_size = 100