from django.shortcuts import redirect
from store.models.product import Product
from django.views import View
from store.models.order import Order
from store.models.customer import Customer


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('no')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_for_cart_by_id(list(cart.keys()))
        print(address,phone,customer,cart,products)

        for product in products:
            order = Order(customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          quantity = cart.get(str(product.id)),
                          address = address,
                          phone = phone)
            order.save()
            request.session['cart']={}
        return redirect('cart')




