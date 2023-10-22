from django.contrib import admin

# Register your models here.
from .models import main_product
from .models import Orders



admin.site.register(main_product)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('phonenumber', 'status', 'timestamp')  # Add any other fields you want to display
    list_filter = ('status',)  # Filter by the 'status' field

    def get_list_filter(self, request):
        if request.GET.get('status') == 'confirm':
            return ('status',)
        return super().get_list_filter(request)

admin.site.register(Orders, OrdersAdmin)
