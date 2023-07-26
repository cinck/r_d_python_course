from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from custom_forms.forms import CustomUserCreationForm
from users.models import User
from django.http import HttpResponse, JsonResponse


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    model = User
    context_object_name = 'users'


class UsersDetailView(DetailView):
    template_name = 'users/users_detail.html'
    model = User
    context_object_name = 'user'


class UsersCreateView(CreateView):
    template_name = 'users/users_create.html'
    model = User
    context_object_name = 'user'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users-list')

