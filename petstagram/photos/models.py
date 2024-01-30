from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from petstagram.pets.models import Pet


class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet/photos',
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=MIN_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    pets = models.ManyToManyField(Pet)
