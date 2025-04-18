from django.contrib import admin
from .models import Category, SubCategory, Tag, News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'created_at', 'updated_at')
    list_filter = ('category', 'subcategory', 'tags', 'created_at')
    search_fields = ('title', 'category__name', 'subcategory__name', 'tags__name')
    
    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': ('title', 'slug', 'image')
        }),
        ('Bogʻliqliklar', {
            'fields': ('category', 'subcategory', 'tags')
        }),
        ('Sanalar', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')  # bu maydonlar readonly bo'ladi

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)
