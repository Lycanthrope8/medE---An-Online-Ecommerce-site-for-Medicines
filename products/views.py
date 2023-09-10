from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import main_product

# Create your views here.
def prod(request, p_name):
    product_details = {
        'name': p_name
    }

    try:
        product = main_product.objects.get(p_name=product_details['name'])
        product.discounted_price = product.p_price - (product.p_price*(product.p_discount/100))	#FOR DISCOUNT
         
    except main_product.DoesNotExist:
        product = None
        

    return render(request, 'product.html', {'product_details': product})






def category(request, p_category):
    products = main_product.objects.filter(p_category=p_category)

    # Calculate the discounted price for each product
    for product in products:
        product.discounted_price = product.p_price - (product.p_price * (product.p_discount / 100))

    context = {
        'product_details': products,
        'category': p_category,
    }

    return render(request, 'category-wise.html', context)
