from django.contrib import admin
from .models import Category, Restaurant, Product, Model3D, MainPageMenu, Text, Text3D, Awards

# Register your models here.
admin.site.register([Category, Restaurant, Product, Model3D, MainPageMenu, Text, Text3D , Awards])
