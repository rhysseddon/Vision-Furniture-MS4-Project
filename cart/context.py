from decimal import Decimal
from django.conf import settings

from products.models import Product


def cart_contents(request):

    cart_items = []
    product_count = 0
    sub_total = 0
    grand_total = sub_total + Product.delivery_cost

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
