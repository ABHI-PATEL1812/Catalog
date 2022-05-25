from rest_framework import viewsets, permissions
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView

from .serializers import AuthorSerializer, BookCatalogSerializer, CategorySerializer
from .models import Category, Author, BookCatalog
from django.db.models import Q


# Create your views here.


class AuthorAPI(CreateAPIView, ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class CreateBookCatalogAPI(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookCatalogSerializer


class CategoryAPI(CreateAPIView, ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GetMostBookSoldByAuthorAPI(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookCatalogSerializer

    def get_queryset(self):
        qs = BookCatalog.objects.filter(author__name=self.request.query_params.get('author_name')).order_by('sold_count')
        return qs[:1]


class GetMostBookSoldByCategoryAPI(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookCatalogSerializer

    def get_queryset(self):
        qs = BookCatalog.objects.filter(category__name=self.request.query_params.get('category_name')).order_by('sold_count')
        return qs[:1]


class SearchBookAPI(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookCatalogSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        qs = BookCatalog.objects.filter(Q(author__name__icontains=search_term) | Q(title__icontains=search_term))
        return qs


class GetBooksByAuthorAPI(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookCatalogSerializer

    def get_queryset(self):
        qs = BookCatalog.objects.filter(author__name=self.request.query_params.get('author_name'))
        return qs