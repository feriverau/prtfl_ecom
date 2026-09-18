from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):
    products = Product.objects.all().order_by("id")
    paginator = Paginator(products,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myapp/index.html',{'page_obj':page_obj})

def detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'myapp/detail.html',{'product':product})

def search(request):

    item_name = request.GET.get("item_name","").strip()

    if item_name:
        products = Product.objects.filter(
            Q(name__icontains=item_name) |
            Q(description__icontains=item_name)
        )
    else:
        products = Product.objects.none()

    paginator = Paginator(products,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "myapp/search.html",
        {
            "page_obj": page_obj,
            "item_name": item_name,
        },
    )


def category(request, slug):

    category = get_object_or_404(Category,slug=slug)

    products = (Product.objects.filter(category=category,active=True).order_by("name"))

    paginator = Paginator(products, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,"myapp/category.html",{"category":category,"page_obj":page_obj,})