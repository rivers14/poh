from django.db import models
from django.db import models

# Create your models here.
class SliderImg(models.Model):
    slide_image = models.ImageField(upload_to='Images/slider', blank=True)

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='Images/category', blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

class Imggal(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='Images/')
    category=models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
