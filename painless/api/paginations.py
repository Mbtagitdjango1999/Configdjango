from rest_framework.pagination import LimitOffsetPagination

class StandardLimitOffsetPagination(LimitOffsetPagination) :
    default_limit = 20
    max_limit = 10
    limit_query_param = 'bagher'
    offset_query_param = 'talebi'