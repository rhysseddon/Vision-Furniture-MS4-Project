from django.shortcuts import render


def view_favorites(request):
    """ A view that will render the favorites page """

    return render(request, 'favorites/favorites.html')
