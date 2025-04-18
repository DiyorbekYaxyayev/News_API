from django.urls import path
from .views import CategoryViewSet, SubCategoryViewSet, TagViewSet, NewsViewSet, LikesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'news', NewsViewSet)
router.register(r'likes', LikesViewSet)

urlpatterns = router.urls
