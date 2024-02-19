from django import forms

from petstagram.pets.forms import ReadonlyFieldsFromMixin
from petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'location', 'pets')


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass


class PetPhotoEditForm(PetPhotoBaseForm, ReadonlyFieldsFromMixin):
    readonly_fields = ("photo", "pets")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()