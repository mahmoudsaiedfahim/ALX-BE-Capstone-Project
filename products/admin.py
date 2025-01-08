from django.contrib import admin
from .models import Category, Product
from django.utils.translation import gettext_lazy as _
# Register your models here.

class PriceRangeFilter(admin.SimpleListFilter):
    title = _('Price Range')
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-100', '0 - 100'),
            ('100-500', '100 - 500'),
            ('500-1000', '500 - 1000'),
            ('1000+', '1000 and above'),
        )
    def queryset(self, request, queryset):
        if self.value() == '0-100':
            return queryset.filter(price__gte=0, price__lte=100)
        if self.value() == '100-500':
            return queryset.filter(price__gte=100, price__lte=500)
        if self.value() == '500-1000':
            return queryset.filter(price__gte=500, price__lte=1000)
        if self.value() == '1000+':
            return queryset.filter(price__gte=1000)
        return queryset


class StockAvailabilityFilter(admin.SimpleListFilter):
    title = _('Stock Availability')
    parameter_name = 'stock_availability'
    
    def lookups(self, request, model_admin):
        return (
            ('in_stock', 'In Stock'),
            ('out_of_stock', 'Out of Stock'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'in_stock':
            return queryset.filter(stock_quantity__gt=0)
        if self.value() == 'out_of_stock':
            return queryset.filter(stock_quantity__lte=0)
        return queryset

class CustomProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'category', 'price','stock_quantity', 'user', 'created_date')
    search_fields = ('name', 'category__name',)
    list_filter = (PriceRangeFilter, StockAvailabilityFilter, 'category')
    
admin.site.register(Category)
admin.site.register(Product, CustomProductAdmin)
