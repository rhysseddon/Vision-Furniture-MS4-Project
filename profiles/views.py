from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import UserProfile, Favorites
from .forms import UserProfileForm
from products.models import Product

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ A view that will render the previous orders"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def view_favorites(request):
    """ A view that will render the favorites page """
    user = UserProfile.objects.get(user=request.user)
    favorites = Product.objects.filter(favorites__user=user)
    context = {
        'favorites': favorites,
    }
    return render(request, 'profiles/favorites.html', context)


def add_to_favorites(request, product_id):
    """ Add products to the favorites page """
    favorite = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    favorites_user, created = Favorites.objects.get_or_create(
        user=user)
    favorites = Product.objects.filter(favorites__user=user)

    if created:
        favorite.favorites.add(favorites_user.id)
        messages.info(request, 'Added product to favorites!')
    else:
        if favorite in favorites:
            favorite.favorites.remove(favorites_user.id)
            messages.info(request, 'Removed product from favorites!')
        else:
            favorite.favorites.add(favorites_user.id)
            messages.info(request, 'Added product to favorites!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
