from django.urls import path
from .views import home
from .views.login import Login, logout
from .views import signup
from .views.cart import Cart
from .views import checkout
from .views.orders import Orders
from store.middlewares.auth import auth_middleware

urlpatterns = [
  path('', home.Index.as_view(), name='homepage'),
  path('signup', signup.Signup.as_view(), name='signup'),
  path('login', Login.as_view(), name='login'),
  path('logout', logout, name='logout'),
  path('cart', Cart.as_view(), name='cart'),
  path('checkout', checkout.Checkout.as_view(), name='checkout'),
  path('orders', auth_middleware(Orders.as_view()), name='orders')

]
