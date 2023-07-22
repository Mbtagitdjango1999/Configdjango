from rest_framework import routers

from .v1.views import CategoryViewSet


router = routers.DefaultRouter()
router.register(r'categories',CategoryViewSet)

urlpatterns = router.urls

# urlpatterns = [
    
# ]

