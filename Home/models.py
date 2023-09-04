from django.db import models

# Create your models here.

class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_category = models.CharField(max_length=255)
    p_image_data = models.BinaryField()  # Assuming you're storing binary image data
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_discount = models.DecimalField(max_digits=5, decimal_places=2)
    p_id = models.AutoField(primary_key=True)