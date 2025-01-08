from django.contrib import admin
from .models import *
# Register your models here.

class SubcategoryTabular(admin.TabularInline):
    model=Subcategory

class CategoryAdmin(admin.ModelAdmin):
    inlines=[SubcategoryTabular]



admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(MainCategory)
admin.site.register(Category,CategoryAdmin)