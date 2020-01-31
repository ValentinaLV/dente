from django.contrib import admin

from .models import ServiceProductCategory, ServiceProduct


class ServiceProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ServiceProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10


admin.site.register(ServiceProductCategory, ServiceProductCategoryAdmin)
admin.site.register(ServiceProduct, ServiceProductAdmin)
