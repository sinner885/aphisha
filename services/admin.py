from django.contrib import admin

from .models import CategoryService, Service

@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    """Категории Услуг"""
    list_display = ('name', 'id', 'slug', 'icon')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    """Услуги"""
    list_display = (
        "id",
        "subject",
        'slug',
        "user",
        "category",
        'name',
        'email',
        "created",
        "moderation",
        'telefon',
        'location'
    )
    list_display_links = ("subject",)
    
    #prepopulated_fields = {"slug": ("user", "subject")}
    search_fields = ("user", "category", "subject", "date", "created")


