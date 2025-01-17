from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('filter-category',views.filter_category,name='filter_category')
] 