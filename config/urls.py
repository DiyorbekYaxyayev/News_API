from django.contrib import admin
from django.urls import path
from news.views import (
    UserRegistrationViewSet,
    UserViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    TagViewSet,
    NewsViewSet,
    LikesViewSet,
    CommentViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', UserRegistrationViewSet.as_view({'post': 'create'}), name='register'),
    path('api/users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('api/categories/', CategoryViewSet.as_view({'get': 'list'}), name='category-list'),
    path('api/subcategories/', SubCategoryViewSet.as_view({'get': 'list'}), name='subcategory-list'),
    path('api/tags/', TagViewSet.as_view({'get': 'list'}), name='tag-list'),
    path('api/news/', NewsViewSet.as_view({'get': 'list'}), name='news-list'),
    path('api/likes/', LikesViewSet.as_view({'get': 'list', 'post': 'create'}), name='like-list'),
    path('api/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
]
