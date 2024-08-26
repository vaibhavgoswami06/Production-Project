from django.db import models
from django.utils import timezone

# Create your models here.
class Members(models.Model):
    name  = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contactno = models.CharField(max_length=12)
    email= models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
       return self.name

# main category
class Maincat(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
       return self.name

# subcategory
class Subcat(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural ='Sub Categories'
     

class Product(models.Model):
    name = models.CharField(max_length=100)
    price =models.DecimalField(default=0,decimal_places=2,max_digits=9)
    maincat = models.ForeignKey(Maincat,on_delete=models.CASCADE, default=1)
    subcat = models.ForeignKey(Subcat,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    rating = models.IntegerField(default=1)
    def __str__(self):
        return self.name