from django.contrib import admin

from .models import Category, Advert

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('name', 'id', 'slug', 'icon')
    prepopulated_fields = {"slug": ("name",)}
    

  
@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
        "id",
        "subject",
        'slug',
        "user",
        "category",
        'types_ad',
        'types_pr',
        'name',
        'email',
        "price",
        "created",
        "moderation",
        'telefon',
        'location'
    )
    list_display_links = ("subject",)
    
    #prepopulated_fields = {"slug": ("user", "subject")}
    search_fields = ("user", "category", "subject", "date", "created")
