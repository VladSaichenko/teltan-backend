from django.contrib import admin

from .models.products import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (
        ProductImageInline,
    )
    readonly_fields = ('tickets_bought', 'tickets_amount', 'ticket_price', 'redemption_percent', 'viewed')


admin.site.register(ProductImage)
