from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):

    products = Product.objects.all().order_by("id")

    paginator = Paginator(products, 4)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    offers = get_offers()

    return render(
        request,
        'myapp/index.html',
        {
            'page_obj': page_obj,
            'offers': offers,
        }
    )

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    compatible_products = get_compatible_products(product)

    return render(request, "myapp/detail.html", {
        "product": product,
        "compatible_products": compatible_products,
    })

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
    category = get_object_or_404(Category, slug=slug)

    subcategories = category.subcategories.all()

    if subcategories.exists():
        return render(request, "myapp/category.html", {
            "category": category,
            "subcategories": subcategories,
        })

    products = Product.objects.filter(
        category=category,
        active=True
    ).order_by("name")

    paginator = Paginator(products, 4)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "myapp/category.html", {
        "category": category,
        "page_obj": page_obj,
    })


def get_compatible_products(product):
    compatible_products = {
        "processors": Product.objects.none(),
        "motherboards": Product.objects.none(),
        "ram": Product.objects.none(),
    }

    if product.product_type == "processor":
        compatible_products["motherboards"] = Product.objects.filter(
            product_type="motherboard",
            socket=product.socket,
            active=True
        )

    elif product.product_type == "motherboard":
        compatible_products["processors"] = Product.objects.filter(
            product_type="processor",
            socket=product.socket,
            active=True
        )

        compatible_products["ram"] = Product.objects.filter(
            product_type="ram",
            memory_type=product.memory_type,
            active=True
        )

    elif product.product_type == "ram":
        compatible_products["motherboards"] = Product.objects.filter(
            product_type="motherboard",
            memory_type=product.memory_type,
            active=True
        )

    return compatible_products

def get_offers():
    return Product.objects.filter(
        active=True,
        is_offer=True
    ).order_by("id")