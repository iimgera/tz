from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = TagSerializer
    serializer_class = TagSerializer
