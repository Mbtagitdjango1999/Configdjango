from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.mixins import (
    ListModelMixin , RetrieveModelMixin,
) 
from sageteam.blog.models import Category
from ..serializers import CategorySerilizer
from rest_framework.pagination import LimitOffsetPagination

from painless.api import StandardLimitOffsetPagination

# class StandardLimitOffsetPagination(LimitOffsetPagination) :
#     default_limit = 20
#     max_limit = 10
#     limit_query_param = 'bagher'
#     offset_query_param = 'talebi'

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer
    #pagination_class = StandardLimitOffsetPagination
    