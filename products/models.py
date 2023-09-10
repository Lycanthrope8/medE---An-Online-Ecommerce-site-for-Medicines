from django.db import models

class main_product(models.Model):
    CATEGORY_CHOICES = (
        ('BABY CARE', 'BABY CARE'),
        ('MENS','MENS')
      )
        
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=255)
    p_type = models.CharField(max_length=255)
    p_generics = models.CharField(max_length=255)
    p_company = models.CharField(max_length=255)
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
    p_category=models.CharField(max_length=255, choices=CATEGORY_CHOICES)

    

    