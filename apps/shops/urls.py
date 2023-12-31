from rest_framework.routers import DefaultRouter

from apps.shops.views import ShopViewSet


router = DefaultRouter()
router.register('', ShopViewSet, "api_shops")

urlpatterns = router.urls