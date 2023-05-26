from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = '1'
    max_page_size = 100