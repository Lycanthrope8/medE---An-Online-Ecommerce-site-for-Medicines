from django.contrib import admin

# Register your models here.
from .models import Product
from authentication.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    # Customize the display in the admin panel if needed
    list_display = ('phone_number',)

# Register the UserProfile model with the custom admin configuration
admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Product)
# admin.site.register(UserProfile)