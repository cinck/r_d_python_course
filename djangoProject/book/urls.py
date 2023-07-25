
from django.urls import path
from book import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='books-list'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
]