from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    View function to display a list of all lettings.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response with the list of lettings.
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    View function to display details of a specific letting.

    Parameters:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: A rendered HTML response with the letting details.
    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
