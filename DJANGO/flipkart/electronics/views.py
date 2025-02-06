from django.shortcuts import render,HttpResponse
from .models import Product

# Create your views here.
def home(request):
    data = Product.objects.all()
    return HttpResponse(data)
