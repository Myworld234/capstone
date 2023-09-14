from django.db import models
from django.contrib.auth.models import User

# User Profile's can be used to modify the default User model, shipped with Django.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)