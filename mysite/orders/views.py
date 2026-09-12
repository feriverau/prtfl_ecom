from django.shortcuts import render,redirect
from .forms import AddressForm
from .models import Address
# Create your views here.

def add_address(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None
    if request.method=="POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect("index")
    form = AddressForm(instance=address)
    return render(request,'orders/add_address.html',{'form':form})