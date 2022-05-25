from django.urls import path, include
from .views import \
    AuthorAPI, CreateBookCatalogAPI, CategoryAPI, GetMostBookSoldByAuthorAPI, \
    GetMostBookSoldByCategoryAPI, SearchBookAPI, GetBooksByAuthorAPI, AuthorNamesAPI


urlpatterns = [
    path('author/', AuthorAPI.as_view(), name='create-author-api'),
    path('author-names/', AuthorNamesAPI.as_view(), name='author-names-api'),
    path('create-book-catalog/', CreateBookCatalogAPI.as_view(), name='create-book-catalog-api'),
    path('category/', CategoryAPI.as_view(), name='category-api'),
    path('get-most-book-sold-by-category/', GetMostBookSoldByCategoryAPI.as_view(), name='get-most-book-sold-by-category-api'),
    path('get-most-book-sold-by-author/', GetMostBookSoldByAuthorAPI.as_view(), name='get-most-book-sold-by-author-api'),
    path('search-book/', SearchBookAPI.as_view(), name='search-book-api'),
    path('get-books-by-author/', GetBooksByAuthorAPI.as_view(), name='get-books-by-author-api'),
]
