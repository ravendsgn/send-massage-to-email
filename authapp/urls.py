from django.urls import path
from .views import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardViewSet, OrderViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
