from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prod(request):
    return render(request,'product.html')
