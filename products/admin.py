from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ProductCategory)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category', 'image')
    # readonly_fields = ('name',)
    search_fields = ('name', '')
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = models.Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0