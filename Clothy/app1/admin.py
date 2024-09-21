from django.contrib import admin
from .models import Members, Maincat, Subcat, Product, Size, Profile
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Members)
admin.site.register(Maincat)
admin.site.register(Subcat)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Profile)

# mix profile info in user table
class ProfileInline(admin.StackedInline):
    model = Profile

# extend the user model

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username","firstname","lastname","email"]
    inlines = [ProfileInline]

# unregisted the old way
admin.site.unregister(User)

# registering the new way
admin.site.register(User, UserAdmin)