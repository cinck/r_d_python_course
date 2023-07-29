
from django.urls import path, include
from book import views
from book.api import views as api_views
from rest_framework import routers


app_name = 'book'

router = routers.SimpleRouter()
router.register('', api_views.BookModelViewSet)

urlpatterns = [
    path('', views.BookListView.as_view(), name='books-list'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('api/', include(router.urls))
]

