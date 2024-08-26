from django.contrib import admin
from .models import Members, Maincat, Subcat, Product
# Register your models here.

admin.site.register(Members)
admin.site.register(Maincat)
admin.site.register(Subcat)
admin.site.register(Product)
