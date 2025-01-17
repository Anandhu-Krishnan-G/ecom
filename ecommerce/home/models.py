from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify           #same for all code , it is copied
from django.db.models.signals import pre_save   #same for all code , it is copied
from django.dispatch import receiver            #same for all code , it is copied


# Create your models here.
class Slider(models.Model):
    CHOICES=(
        ('New Deal','New Deal'),
        ('New Arrivals','New Arrivals'),
        ('Hot Deals','Hot Deals'),
        ('Best Seller','Best Seller')
    )
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='Images/sliderjpg')
    deal=models.CharField(choices=CHOICES,max_length=250)
    discount=models.PositiveBigIntegerField(default=0,null=True)
    link=models.CharField(max_length=250,default='#',null=True)

    def __str__(self):
        return self.title[:50]


class Banner(models.Model):
    CHOICES=(
        ('Intelligent New Touch Control','IntelligentNew Touch Control'),
        ('On-sale Best Prices','On-sale Best Prices'),
        ('Hot Sale Super Laptops 2022','Hot Sale Super Laptops 2025')
    )
    title=models.CharField(choices=CHOICES,max_length=250)
    image=models.ImageField(upload_to='Images/banner.jpg')
    discount=models.PositiveBigIntegerField(default=0,null=True)

    def __str__(self):
        return self.title
    

class MainCategory(models.Model):
    title=models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title=models.CharField(max_length=250)
    mainCategory=models.ForeignKey(MainCategory,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=250,null=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    price=models.PositiveBigIntegerField(default=0,null=True)
    discount=models.PositiveBigIntegerField(default=0,null=True)
    featured_image=models.CharField(max_length=250)
    brand=models.CharField(max_length=250,null=True)
    total=models.PositiveBigIntegerField(default=0,null=True)
    available=models.PositiveBigIntegerField(default=0,null=True)
    description=RichTextField(null=True,blank=True)
    product_information=RichTextField(null=True,blank=True)
    tags=models.CharField(max_length=250,blank=True)
    slug=models.CharField(max_length=250,blank=True)


    def __str__(self):
        return self.title[:40]
    
    
@receiver(pre_save,sender=Product)
def generate_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        base_slug=slugify(instance.title)
        unique_slug=base_slug
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug=f"{base_slug}-{instance.id}"
        instance.slug=unique_slug


class Additional_infromation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,null=True,blank=True)
    spec=models.CharField(max_length=250,null=True,blank=True)

class Additional_image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.CharField(max_length=600,null=True,blank=True)
