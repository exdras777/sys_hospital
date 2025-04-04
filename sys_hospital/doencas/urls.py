from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoencasViewSet

router = DefaultRouter()
router.register(r'doencas', DoencasViewSet, basename='doenca')

urlpatterns = [
    path('', include(router.urls)),
]