from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def cart_add(request):
    print("Botón del carro clickeado")
    if request.method=="POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("El producto agregado tiene la id:",product_id)
        print("La cantidad del producto es:",product_quantity)
    return JsonResponse({'Message':'Botón del carro clickeado'})
