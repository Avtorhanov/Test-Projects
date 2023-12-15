from django.contrib import admin
from .models import Category, Sub_category, Product

admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Product)