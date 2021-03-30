def favorites_contents(request):

    favorites_items = []

    context = {
        'favorites_items': favorites_items,
    }

    return context
