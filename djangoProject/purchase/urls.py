
from django.urls import path
from purchase import views

app_name = 'purchase'

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchase-list'),
    path('<int:pk>', views.PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create/', views.PurchaseCreateView.as_view(), name='purchase-create'),
]