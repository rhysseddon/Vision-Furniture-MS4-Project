from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Room

# Create your views here.


def all_products(request):
    """ A view that shows all products with sorting and searching """

    products = Product.objects.all()
    query = None
    rooms = None

    if request.GET:
        if 'room' in request.GET:
            rooms = request.GET['room'].split(',')
            products = products.filter(room__name__in=rooms)
            rooms = Room.objects.filter(name__in=rooms)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_rooms': rooms,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view that shows products individually with added details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
