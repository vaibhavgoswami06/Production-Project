from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#creating a Customer Profile
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    pincode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.User.username

# create a user Profile by default when user sign up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(User=instance)
        user_profile.save()

# automate the profile thing
post_save.connect(create_profile, sender=User)






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
     
class Size(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price =models.DecimalField(default=0,decimal_places=2,max_digits=9)
    maincat = models.ForeignKey(Maincat,on_delete=models.CASCADE, default=1)
    subcat = models.ForeignKey(Subcat,on_delete=models.CASCADE, default=1)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    rating = models.IntegerField(default=1)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    def __str__(self):
        return self.name