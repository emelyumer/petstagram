from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models
from django.utils import timezone


'''
Auth in Django
1.Use built-in user - by default
2.Use built-in user only for auth and define "Profile" model for user data
3.Define a custom user model for auth and define "Profile" model for user data
'''


class PetstagramUser(auth_models.AbstractBaseUser):
    #password from AbstractBaseUser
    #last_login from AbstractBaseUser

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exist")
        }
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
