from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()

router.register('authors', UserViewSet, basename='authors')


urlpatterns = router.urls
