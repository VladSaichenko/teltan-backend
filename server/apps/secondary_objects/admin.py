from django.contrib import admin

from .models.for_products import Category
from .models.locational import Country, City, Address, Street

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Street)
admin.site.register(City)
admin.site.register(Address)
