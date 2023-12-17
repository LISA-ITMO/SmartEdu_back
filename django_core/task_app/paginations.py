from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 50
    page_query_param = "page_size"
    max_page_size = 250
