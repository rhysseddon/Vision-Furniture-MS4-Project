from django.shortcuts import render
from .models import Help


def index(request):
    """ A view that will return the index page """

    return render(request, 'home/index.html')


def help_centre(request):
    """ A view that will render the help centre page """
    help_info = Help.objects.all()
    context = {
        'help_info': help_info
    }
    return render(request, 'home/help_centre.html', context)
