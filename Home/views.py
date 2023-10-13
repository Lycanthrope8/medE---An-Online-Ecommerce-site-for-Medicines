from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    for product in products:

        product.discounted_price = product.p_price - (product.p_price*(product.p_discount/100))	#FOR DISCOUNT

    return render(request,'index.html',{'products': products})

def profile(request):
    return render(request,'user-profile.html')


