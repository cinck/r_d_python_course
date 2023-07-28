
from django.urls import path, include
from book import views
from rest_framework import routers


app_name = 'book'

router = routers.SimpleRouter()
router.register('', views.BookViewSet)

urlpatterns = [
    path('', views.BookListView.as_view(), name='books-list'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('', include(router.urls))
]
