from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    View function to display a list of all profiles.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response with the list of profiles.
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """
    View function to display details of a specific user profile.

    Parameters:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile to display.

    Returns:
        HttpResponse: A rendered HTML response with the profile details.
    """

    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
