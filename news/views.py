from django.shortcuts import render
from .models import User, Category, SubCategory, Tag, News, Likes, Comment
from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer, SubCategorySerializer, TagSerializer, NewsSerializer, LikeSerializer, CommentSerializer, RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

User = get_user_model()

class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['id', 'name']        
    search_fields = ['name']                  
    ordering_fields = ['id', 'name']          
    ordering = ['-id']                      

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['id', 'title', 'category', 'subcategory', 'tags']
    search_fields = ['title', 'category__name', 'subcategory__name', 'tags__name']

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id', 'news', 'user']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id', 'news', 'user']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['id', 'username', 'email']
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    
class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'username', 'email']
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'username']
    
    def perform_create(self, serializer):
        # Create the user with the given data
        serializer.save()

class JWTTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class JWTTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

