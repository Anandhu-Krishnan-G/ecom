from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    slider=Slider.objects.all()[:3]
    banner=Banner.objects.all()[:3]
    mainCategory=MainCategory.objects.all()
    context={
        'slider':slider,
        'banner':banner,
        'category':mainCategory
    }
    return render(request,'home.html',context)