from django.shortcuts import render


def view_cart(request):
    """ A view that will render the cart contents page """

    return render(request, 'cart/cart.html')
