from django.contrib import admin
from .models import Category, Product, ProductImage, ColorVariant, SizeVariant
# Register your models here.
admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price' ]
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color', 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size', 'price']
    model = SizeVariant

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)