from django.contrib import admin
from .models import Category, Imggal, SliderImg

# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    ordering = ('category',)
admin.site.register(Category)
admin.site.register(Imggal,ImgAdmin)
admin.site.register(SliderImg)
