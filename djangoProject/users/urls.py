from django.urls import path
from users import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name='users-list'),
    path('<int:pk>', views.UsersDetailView.as_view(), name='users-detail'),
    path('create/', views.UsersCreateView.as_view(), name='users-create'),
]
