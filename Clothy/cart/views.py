from django.shortcuts import render, get_object_or_404
from .cart import Cart
from app1.models import Product
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total = cart.cart_total()
    return render(request, 'cart_summary.html', {"cart_products":cart_products,"quantities":quantities,"totals":total})


def cart_add(request):
    #get the cart
    cart = Cart(request)
    # test for Post
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product_size = str(request.POST.get('product_size'))
        print(product_quantity)
        # lookup product in database
        product = get_object_or_404(Product, id=product_id)
        print(product)
        # save to session
        cart.add(product=product, quantity=product_quantity, size=product_size)
        #get cart quantity
        cart_quantity = cart.__len__()

        # Return response
        #response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Item has been added"))
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'message': product_id})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, quantity = product_quantity)
        response = JsonResponse({'qty': product_quantity})
        messages.success(request, ("cart has been updated"))
        return response