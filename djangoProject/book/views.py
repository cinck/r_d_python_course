from django.views.generic import ListView, DetailView

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

    # def get(self, request, *args, **kwargs):
    #     try:
    #         obj = Book.objects.get(id=kwargs.get('pk'))
    #         return render(request, 'book/book_list.html', {'object': obj})
    #     except Book.DoesNotExist:
    #         raise Http404(f"{kwargs.get('pk')} does not exist")


# <HW37> Task 4. JSON response
# def json_books(request):
#     if request.method == "GET":
#         response_list = list(Book.objects.all().values())
#         return JsonResponse(response_list, safe=False)
