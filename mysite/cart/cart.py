from myapp.models import Product
from decimal import Decimal

class Cart():
    def __init__(self,request):
        self.session =  request.session
        cart = request.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart']={}
        self.cart = cart

    def __len__(self):
        return sum (int(item['qty']) for item in self.cart.values())

    def get_build_status(self):
        products = Product.objects.filter(
            id__in=self.cart.keys()
        )

        processor = next(
            (product for product in products if product.product_type == "processor"),
            None
        )

        motherboard = next(
            (product for product in products if product.product_type == "motherboard"),
            None
        )

        ram = next(
            (product for product in products if product.product_type == "ram"),
            None
        )

        processor_compatible = True
        ram_compatible = True

        motherboard_warnings = []
        processor_message = None
        ram_message = None

        if processor and motherboard:
            if processor.socket != motherboard.socket:

                processor_compatible = False

                processor_message = (
                    f"Tu placa utiliza {motherboard.socket}, "
                    f"pero este procesador utiliza {processor.socket}."
                )

                motherboard_warnings.append(
                    f"Esta placa utiliza {motherboard.socket}, "
                    f"pero el procesador seleccionado utiliza {processor.socket}."
                )

        if motherboard and ram:
            if motherboard.memory_type != ram.memory_type:

                ram_compatible = False

                ram_message = (
                    f"Tu placa utiliza {motherboard.memory_type}, "
                    f"pero esta RAM utiliza {ram.memory_type}."
                )

                motherboard_warnings.append(
                    f"Esta placa utiliza {motherboard.memory_type}, "
                    f"pero la RAM seleccionada utiliza {ram.memory_type}."
                )

        return {
            "processor": processor is not None,
            "motherboard": motherboard is not None,
            "ram": ram is not None,

            "processor_compatible": processor_compatible,
            "motherboard_compatible": True,
            "ram_compatible": ram_compatible,

            "processor_message": processor_message,
            "motherboard_warnings": motherboard_warnings,
            "ram_message": ram_message,
        }

    def get_total_price(self):
        return sum(Decimal(item['price']) * Decimal(item['qty']) for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product']=product

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['qty']=Decimal(item['qty'])
            item['total']=item['price']*item['qty']
            yield item

    def add(self,product,product_qty):
        product_id = product.id
        if product_id in self.cart:
            self.cart[product_id]['qty']= product_qty
        else:
            self.cart[product_id]={'price':str(product.price),'qty':product_qty} 
        self.session.modified=True

    def delete(self,product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified=True

    def update(self,product,qty):
        product_id = str(product)
        product_quantity = qty
        if product_id in self.cart:
            self.cart[product_id]['qty']=product_quantity
        self.session.modified=True