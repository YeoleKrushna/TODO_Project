from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Books
from .forms import BooksForm
# Create your views here.
def home(request):
    books = None
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        data = Books.objects.all()
    else:
        form = BooksForm()
        books = Books.objects.all()


    
    return render(request, 'books/home.html',{'books':books,'form':form})
