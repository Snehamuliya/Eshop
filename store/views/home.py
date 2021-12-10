from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('pid')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
            # here 1 is quantity and product is product id of cart
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
    
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        #del request.session['cart']
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        user = request.session.get('email')
        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['s_user'] = user
        print('you are: ', request.session.get('email'))
        return render(request, 'index.html', data)
        return render(request, 'header.html', data)
        return render(request, 'cart.html', data)










