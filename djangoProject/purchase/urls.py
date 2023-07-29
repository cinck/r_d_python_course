
from django.urls import path, include
from rest_framework import routers
from purchase.api import views as api_views
from purchase import views

app_name = 'purchase'

router = routers.SimpleRouter()
router.register('', api_views.PurchaseModelViewSet)

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchase-list'),
    path('<int:pk>', views.PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create/', views.PurchaseCreateView.as_view(), name='purchase-create'),
    path('api/', include(router.urls))
]