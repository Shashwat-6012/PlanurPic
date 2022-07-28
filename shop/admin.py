from django.contrib import admin

# Register your models here.
from .models import category, Product

admin.site.register(category)
admin.site.register(Product)
