from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from purchase.models import Purchase
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


class PurchaseListView(ListView):
    template_name = 'purchase/purchase_list.html'
    model = Purchase
    context_object_name = 'purchases'


class PurchaseDetailView(DetailView):
    template_name = 'purchase/purchase_detail.html'
    model = Purchase
    context_object_name = 'purchase'


class PurchaseCreateView(CreateView):
    template_name = 'purchase/purchase_create.html'
    model = Purchase
    context_object_name = 'purchase'
    fields = ('book', 'user')
    success_url = reverse_lazy('purchase:purchase-list')

# <HW37> Task 4. JSON response
def json_purchases(request):
    if request.method == "GET":
        response_list = list(Purchase.objects.all().values())

        return JsonResponse(response_list, safe=False)
