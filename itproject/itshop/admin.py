from django.contrib import admin
from . models import Category, Product, Customer, Order

# Register your models here.

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name','purchage_price', 'sell_price', 'discount')
    list_filter=('category',)

admin.site.register(Product, ProductAdmin)


