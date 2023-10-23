from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from products.models import Orders
from authentication.models import UserProfile
from products.models import Profile_MedList
import ast
from products.models import main_product 
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


def quick_order(request):
    phonenumber = request.user.phone_number
    user_address = request.user.address
    saved_data = Profile_MedList.objects.filter(phone_number=phonenumber).values()
    data_list = list(saved_data)
    med_list = data_list[0]['med_list']
    counter=0
    t=[]
    total=0
    for key,value in med_list.items():
        morning_day_len = len(med_list[key][0])  # Length of ['Morning', 'Day']
        dayy = med_list[key][1]  # The value 5
        products_data = main_product.objects.filter(p_id=int(key)).values('p_name', 'medPerStrip', 'p_price','p_discount')
        medPerStrip = products_data[counter]['medPerStrip']
        price=(products_data[counter]['p_price'] - (products_data[counter]['p_price']*(products_data[counter]['p_discount']/100)))/medPerStrip
        quantity=(products_data[counter]['medPerStrip']*morning_day_len*dayy)/10
        t.append((products_data[counter]['p_name'], str(int(quantity)), '{:.2f}'.format(float(price * quantity))))         
        total+=round(price*quantity,2)

    if(total>0):
        total+=60
    context={'product_data_list': t, 'total': total, 'user_address': user_address}
    print(context)
    return render(request, 'order_confirm.html', context)

    

    


