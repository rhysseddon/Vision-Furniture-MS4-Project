from django.shortcuts import get_object_or_404

from products.models import Product


def cart_contents(request):

    cart_items = []
    product_count = 0
    sub_total = 0
    delivery = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        sub_total += quantity * product.price
        if sub_total >= 400:
            delivery = 40
        elif sub_total >= 150:
            delivery = 25
        elif sub_total >= 50:
            delivery = 10
        elif sub_total >= 20:
            delivery = 7
        else:
            delivery = 5
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'delivery': delivery,
        })

    grand_total = delivery + sub_total

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
