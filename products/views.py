from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from .models import main_product
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import UserProfile
import json

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
        

    if request.user.is_authenticated:
        # Check if the user is logged in
            try:
                user_profile = UserProfile.objects.get(pk=request.user.id)
                if user_profile.user_type == 'quantity':
                    # Check if the user's type is 'quantity'
                    return render(request, 'product.html', {'product_details': product})
            except UserProfile.DoesNotExist:
                pass  # Handle the case where the user profile does not exist
    # Default case if the user is not logged in or their type is not 'quantity'
    return render(request, 'product_day.html', {'product_details': product})






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


def live_search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        results = main_product.objects.filter(p_name__icontains=query)

        # Convert the queryset to a list of dictionaries
        results_list = [
            {
                'p_name': product.p_name,
                'p_type': product.p_type,
            }
            for product in results
        ]

        return JsonResponse(results_list, safe=False)
    


def get_product_info(request, p_id):
    try:
        # Use get() to retrieve a single product by p_id
        product = main_product.objects.get(p_id=p_id)

        # Create a dictionary with the product information
        product_data = {
            'p_id': p_id,
            'p_name': product.p_name,
            'p_category': product.p_category,
            'p_price': str(product.p_price),
            'p_discount': str(product.p_discount),
            'discounted_price':product.p_price - (product.p_price * (product.p_discount / 100)),
            'medPerStrip':product.medPerStrip,
            'p_image':str(product.p_image),
            # Add other fields as needed
        }
        return JsonResponse(product_data)
    
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)





def checkout_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            # Process the cart_data as needed (e.g., complete the checkout)
            output={}
            total=0
            for key, value in data.items():
                product = main_product.objects.get(p_id=key)
                total+=value*((product.p_price - (product.p_price * (product.p_discount / 100)))/product.medPerStrip)
                output[product.p_name]=str(value)+";"+ str(value*(product.p_price - (product.p_price * (product.p_discount / 100)))/product.medPerStrip)
            print(output)
            if(total>0):
                total+=60
            request.session['checkout_output'] = output
            request.session['checkout_total'] = str(total)

            # You can return a JSON response to the client (e.g., JSON response)
            return JsonResponse({'message': 'Checkout successful'})

        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except main_product.DoesNotExist:
            # Handle product not found error
            return JsonResponse({'error': 'Product not found'}, status=404)

    # For other HTTP methods (e.g., GET), return a method not allowed response
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)


def order_confirm(request):
    output = request.session.get('checkout_output')
    total = request.session.get('checkout_total')
    User = UserProfile()
    # Split the product data and create a list of tuples (product_name, quantity, price)
    product_data_list = [(product_name, *product_data.split(';')) for product_name, product_data in output.items()]
    user_address = request.user.address
    context = {'product_data_list': product_data_list, 'total': total,'user_address': user_address}
    print(context)
    return render(request, 'order_confirm.html', context)