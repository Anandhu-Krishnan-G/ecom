from django.db import models

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