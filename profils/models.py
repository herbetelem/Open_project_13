from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A model to extend the user profile with additional information.

    Attributes:
        user (OneToOneField): A reference to the associated user.
        favorite_city (CharField): The user's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
