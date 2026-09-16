from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/index.html',{'page_obj':page_obj})

def detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'myapp/detail.html',{'product':product})