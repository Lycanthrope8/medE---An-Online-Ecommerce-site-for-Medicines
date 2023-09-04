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
    except main_product.DoesNotExist:
        product = None

    return render(request, 'product.html', {'product_details': product})

