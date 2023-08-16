from django.shortcuts import render


def index(request):
    """
    View function to display the index page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response for the index page.
    """

    return render(request, 'index.html')

def custom_404(request, exception):
    """
    View function to display a custom 404 error page.

    Parameters:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: A rendered HTML response for the custom 404 error page.
    """

    return render(request, '404.html', status=404)


def custom_500(request, exception):
    """
    View function to display a custom 500 error page.

    Parameters:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 500 error.

    Returns:
        HttpResponse: A rendered HTML response for the custom 500 error page.
    """
    
    return render(request, '500.html', status=500)