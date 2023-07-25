from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from ..views import user



router = routers.DefaultRouter()
# router.register('1', views.CourseView)
router.register('user', user.UserView)



urlpatterns = [
	path('v1/', include(router.urls)),
	
	
	path("register/", user.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", user.UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", user.UserLogoutAPIView.as_view(), name="logout-user"),
    path("user-info/", user.UserAPIView.as_view(), name="user-info"),

 
 
	# path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	# path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
