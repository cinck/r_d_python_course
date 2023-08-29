from django.urls import path, include
from rest_framework import routers
from users.api import views as api_views
from users import views

app_name = 'users'

router = routers.SimpleRouter()
router.register('', api_views.UserModelViewSet)

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users-list'),
    path('<int:pk>', views.UsersDetailView.as_view(), name='users-detail'),
    path('create/', views.UsersCreateView.as_view(), name='users-create'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='users-delete'),
    path('api/', include(router.urls))
]
