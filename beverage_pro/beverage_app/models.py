from django.db import models

# Create your models here.
class Beverage(models.Model):       
    beverage_title = models.CharField(max_length=100, blank=True, null=True)
    beverage_description = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return str(self.beverage_title )

