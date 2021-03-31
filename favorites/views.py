from django.shortcuts import render, redirect


def view_favorites(request):
    """ A view that will render the favorites page """

    return render(request, 'favorites/favorites.html')


def add_to_favorites(request, item_id):
    """ Add products to the favorites page """
    redirect_url = request.POST.get('redirect_url')
    favorites = request.session.get('favorites', {})

    if item_id in list(favorites.keys()):
        favorites[item_id] 
        # message already added
    else:
        favorites[item_id] 
        # message added to favorites
    request.session['favorites'] = favorites
    print(request.session['favorites'])
    return redirect(redirect_url)
