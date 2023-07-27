from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from book.models import Book
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render


class BookListView(ListView):
    template_name = 'book/book_list.html'
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    context_object_name = 'book'
    fields = ('title', 'author', 'year', 'price')
    success_url = reverse_lazy('book:books-list')

