from django.urls import path
from core.models import Product, Category, CartOrder, CartOrderProducts, wishlist_model 
from django.contrib import messages


def default(request):
    categories = Category.objects.all()

    if request.user.is_authenticated:
        try:
            wishlist = wishlist_model.objects.filter(user=request.user)
        except:
            messages.warning(request, "You need to login before accessing your wishlist.")
            wishlist = 0
    else:
        wishlist = 0

    return {
        'categories':categories,
        'wishlist':wishlist,
    }