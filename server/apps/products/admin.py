from django.contrib import admin

from .models.products import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (
        ProductImageInline,
    )


admin.site.register(ProductImage)
