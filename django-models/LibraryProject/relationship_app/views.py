from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic import DetailView

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context