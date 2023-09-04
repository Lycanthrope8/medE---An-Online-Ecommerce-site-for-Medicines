from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prod(request,p_name):
    product_details = {
        'name': p_name
    
        # Add other product details here
    }
    
    return render(request,'product.html',{'product_details': product_details})
