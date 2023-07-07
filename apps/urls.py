from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.views import BookModelViewSet

router = DefaultRouter()
router.register('book', BookModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]