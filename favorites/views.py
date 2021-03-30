from django.shortcuts import render, redirect


def view_favorites(request):
    """ A view that will render the favorites page """

    return render(request, 'favorites/favorites.html')


# def add_to_favorites(request, item_id):
#     """ Add products to the favorites page """
#     redirect_url = request.POST.get('redirect_url')
#     favorites = request.session.get('favorites', {})
#     print(request.session['favorites'])

#     return redirect(redirect_url)
