from django.contrib import admin

from .models import Carrinho, CarItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ["car_id", "date_added"]

class CartItemAdmin(admin.ModelAdmin):
    list_display = ["produto", "car", "quant"]

admin.site.register(Carrinho, CartAdmin)
admin.site.register(CarItem, CartItemAdmin)
