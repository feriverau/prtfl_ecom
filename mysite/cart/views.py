from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart
from myapp.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.

def cart_add(request):
    cart = Cart(request)
    print("Botón del carro clickeado")
    if request.method=="POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("El producto agregado tiene la id:",product_id)
        print("La cantidad del producto es:",product_quantity)
        #product = Product.objects.get(id=product_id)
        product = get_object_or_404(Product,id=product_id)
        cart.add(product=product,product_qty=product_quantity)
        cart_quantity = cart.__len__()
    return JsonResponse({'qty':cart_quantity})
