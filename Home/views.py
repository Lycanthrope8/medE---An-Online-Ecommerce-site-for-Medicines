from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from products.models import Orders
from authentication.models import UserProfile
from products.models import Profile_MedList
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

    # Medlist  From here

    
    # print('User Phone Number:', phonenumber)  # Check the user phone number in Django console

    # Assuming 'phone_number' is the field name in your Profile_MedList model
    saved_data = Profile_MedList.objects.filter(phone_number=phonenumber).values()

    # Convert the QuerySet to a list of dictionaries
    data_list = list(saved_data)
    # print(data_list)

    return render(request, 'user-profile.html', {'temp': temp,'medList': data_list})



