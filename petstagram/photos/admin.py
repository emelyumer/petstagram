from django.contrib import admin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass

