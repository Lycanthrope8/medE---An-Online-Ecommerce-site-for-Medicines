from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from Home.models import Product

class main_product(models.Model):
    CATEGORY_CHOICES = (
        ('BABY CARE', 'BABY CARE'),
        ('MENS','MENS'),
        ('Cold & Allergies','Cold & Allergies'),
        ('Heart Problems','Heart Problems'),
        ('Diabetes','Diabetes'),
        ('Respiratory Problems','Respiratory Problems'),
        ('Neurological Problems','Neurological Problems'),
        ('Arthritis or other types of pain','Arthritis or other types of pain'),
        ('Sexual Wellness','Sexual Wellness'),
        ('Herbal & Ayurvedic','Herbal & Ayurvedic'),
        ('Infant & Mothers care','Infant & Mothers care'),
        ('Supplements & Nutrition','Supplements & Nutrition')
        

    )
    feature_CHOICES = (('yes', 'yes'), ('no', 'no'))

    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=255)
    p_type = models.CharField(max_length=255)
    p_image=models.ImageField(upload_to='media/',default='static\cat-icons\syringe.png')  # 'images/' is the upload directory
    p_generics = models.CharField(max_length=255)
    p_company = models.CharField(max_length=255)

    medPerStrip = models.DecimalField(max_digits=10, decimal_places=2)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)

    p_discount = models.DecimalField(max_digits=5, decimal_places=2)
    p_Indications = models.TextField()
    p_Pharmacology = models.TextField()
    p_Dosage = models.TextField()
    p_Interaction = models.TextField()
    p_Contradictions = models.TextField()
    p_Side_Effects = models.TextField()
    p_Pregnancy = models.TextField()
    p_Precautions = models.TextField()
    p_Therapeutic = models.TextField()
    p_Storage = models.CharField(max_length=255)
    p_category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    feature = models.CharField(max_length=255, choices=feature_CHOICES)

    def __str__(self):
        return self.p_name

    def save(self, *args, **kwargs):
        super(main_product, self).save(*args, **kwargs)
        if self.p_image and not self.p_image._committed:
            super(main_product, self).save(*args, **kwargs)
        # Check if the feature is 'yes' and create a corresponding Product entry
        if self.feature == 'yes':
            Product.objects.create(
                p_name=self.p_name,
                p_category=self.p_category,
                p_price=self.p_price,
                p_discount=self.p_discount,
                p_id=self.p_id,
                p_image=self.p_image
            )

    def delete(self, *args, **kwargs):
        # Delete the associated Product when deleting main_product
        if self.feature == 'yes':
            try:
                product_to_delete = Product.objects.get(p_id=self.p_id)
                product_to_delete.delete()
            except Product.DoesNotExist:
                pass  # Handle the case where the Product does not exist

        super(main_product, self).delete(*args, **kwargs)

@receiver(pre_save, sender=main_product)
def delete_product_if_feature_changed(sender, instance, **kwargs):
    # Check if the 'feature' field is transitioning from 'yes' to 'no'
    if instance.pk and instance.feature == 'no':
        try:
            product_to_delete = Product.objects.get(p_id=instance.p_id)
            product_to_delete.delete()
        except Product.DoesNotExist:
            pass  # Handle the case where the Product does not exist

# Register the signal
pre_save.connect(delete_product_if_feature_changed, sender=main_product)
