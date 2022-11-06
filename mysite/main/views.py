from django.shortcuts import render
from .models import Category,Imggal,SliderImg

# Create your views here.
def main(request):
    slide = SliderImg.objects.all()
    categories = Category.objects.all()
    return render(request,'main/index.html',{'categories': categories,'slide': slide})



def get_category(request, category_id):
    imgg = Imggal.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    return render(request,'main/galer.html',{'imgg': imgg,
                                                    'categoryes': categories,
                                                    'category': category ,})

def error_404(request,exception):
    return render(request,'404.html')
