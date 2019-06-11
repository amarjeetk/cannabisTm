from django.contrib import admin

# Register your models here.

from .models import Location, Period, Product, Business, Sale, InventoryFinished, InventoryUnfinished 
 
admin.site.register(Location) 
admin.site.register(Period) 
admin.site.register(Product) 
admin.site.register(Business) 
admin.site.register(Sale)
admin.site.register(InventoryFinished) 
admin.site.register(InventoryUnfinished)  