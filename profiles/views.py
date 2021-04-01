from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from .forms import UserProfileForm

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


def order_history(request, order_number):
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


def view_favorites(request):
    """ A view that will render the favorites page """

    return render(request, 'profiles/favorites.html')


def add_to_favorites(request, item_id):
    """ Add products to the favorites page """
    redirect_url = request.POST.get('redirect_url')
    favorites = request.session.get('favorites', {})

    if item_id in list(favorites.keys()):
        favorites[item_id] = 1
        # message already added
    else:
        favorites[item_id] = 1
        # message added to favorites
    request.session['favorites'] = favorites
    print(request.session['favorites'])
    return redirect(redirect_url)
