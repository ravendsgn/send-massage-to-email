# from django.urls import path
# from .views import AuthView

# urlpatterns = [
#     path('auth/', AuthView.as_view(), name='auth'),
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CardViewSet, OrderViewSet, LikeViewSet

# router = DefaultRouter()
# router.register(r'cards', CardViewSet)
# router.register(r'orders', OrderViewSet)
# router.register(r'likes', LikeViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from .views import RegisterView, LogoutView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
]
