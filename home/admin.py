from django.contrib import admin
from .models import ProductModel, PostModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(PostModel)