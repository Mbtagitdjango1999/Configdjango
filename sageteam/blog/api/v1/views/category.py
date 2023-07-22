from rest_framework.viewsets import ModelViewSet
from sageteam.blog.models import Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.