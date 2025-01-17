from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    slider=Slider.objects.all()[:3]
    banner=Banner.objects.all()[:3]
    mainCategory=MainCategory.objects.all()
    product=Product.objects.all()
    context={
        'slider':slider,
        'banner':banner,
        'category':mainCategory,
        'products':product
    }
    return render(request,'home.html',context)

def shop(request):
    slider=Slider.objects.all()[:3]
    banner=Banner.objects.all()[:3]
    category=Category.objects.all()
    product=Product.objects.all()
    context={
        'slider':slider,
        'banner':banner,
        'category':category,
        'products':product
    }
    return render(request,'product-view.html',context)


def filter_category(request):
    product=Product.objects.all()
    if request.method=='POST':
        jsondata=json.loads(request.body.decode("utf-8"))
        req=jsondata.get('categories')
        product=Product.objects.filter(category__id__in=req).distinct()
        context={
            "products":product,
        }
        data=render_to_string('includes/ajax/product-filter.html',context)
    return JsonResponse({"status":"Success","data":data})
