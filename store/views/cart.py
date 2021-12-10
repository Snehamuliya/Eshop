from django.shortcuts import render
from store.models.product import Product
from django.views import View


class Cart(View):
    def get(self, request):
        ids = (list(request.session.get('cart').keys()))
        products = Product.get_product_for_cart_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products' : products})

