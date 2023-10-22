from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from products.models import Orders
from authentication.models import UserProfile
import ast
# Create your views here.
def home(request):
    products = Product.objects.all()
    for product in products:

        product.discounted_price = product.p_price - (product.p_price*(product.p_discount/100))	#FOR DISCOUNT

    return render(request,'index.html',{'products': products})



def profile(request):
    User = UserProfile()
    phonenumber = request.user.phone_number
    orders = Orders.objects.filter(phonenumber=phonenumber) 
    temp={}
    for i in orders:
        d=[]
        data=ast.literal_eval(i.ordered_products)
        for item in data:
            name, number, _ = item
            d.append(str(name+"X"+number))


        temp[i.id]=[d,i.total,i.timestamp,i.status]
    return render(request, 'user-profile.html', {'temp': temp})



