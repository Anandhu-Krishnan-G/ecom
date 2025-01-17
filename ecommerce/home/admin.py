from django.contrib import admin
from .models import *
# Register your models here.

class SubcategoryTabular(admin.TabularInline):
    model=Subcategory

class CategoryAdmin(admin.ModelAdmin):
    inlines=[SubcategoryTabular]




class AdditionalinfoTabular(admin.TabularInline):
    model=Additional_infromation

class AdditionalImageTabular(admin.TabularInline):
    model=Additional_image

class ProductAdmin(admin.ModelAdmin):
    inlines=[AdditionalinfoTabular,AdditionalImageTabular]





admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(MainCategory)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)