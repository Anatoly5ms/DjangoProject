from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin): # an easy way to create a User model: no need to write the code, Django will do it
    
    def __str__(self):
        return "@{}".format(self.username)