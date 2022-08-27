from django.urls import path
from .views import (
    
    BookListAPIView,
    BookRetriveAPIView,
    BookCreateAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
)

urlpatterns = [
    path("list/", BookListAPIView.as_view(), name="list_book"),#for list of books
    path("list/<pk>/", BookRetriveAPIView.as_view()), # to retrive single book
    path("list/<pk>/remove/", BookDeleteAPIView.as_view()),#to delete book
    path("create/", BookCreateAPIView.as_view()),#to create book info
    path("list/<pk>/update/",BookUpdateAPIView.as_view()),#to update book
]