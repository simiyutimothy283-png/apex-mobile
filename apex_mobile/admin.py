from django.contrib import admin
from .models import Category, Product, RegisteredClient

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock', 'is_featured', 'is_top_deal', 'warranty_info')
    list_filter = ('brand', 'is_featured', 'is_top_deal', 'category')
    list_editable = ('price', 'stock', 'is_featured', 'is_top_deal')  # Allows instant updates directly from the list view
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'brand', 'storage', 'color')
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'slug', 'brand', 'price', 'image', 'description')
        }),
        ('Technical Specifications', {
            'fields': ('storage', 'ram', 'color', 'warranty_info', 'stock')
        }),
        ('Marketing & Visibility', {
            'fields': ('is_featured', 'is_top_deal')
        }),
    )


@admin.register(RegisteredClient)
class RegisteredClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'registered_at')
    search_fields = ('name', 'email', 'phone_number')
    readonly_fields = ('registered_at',)
    list_per_page = 30