from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from petstagram.photos.forms import PetPhotoCreateForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/create_photo.html"

    def get_success_url(self):
        return reverse('details photo', kwargs={
            "pk": self.object.pk,
        })


class PetPhotoDetailView(views.DetailView):
    queryset = PetPhoto.objects.all()
    template_name = "photos/details_photo.html"


def edit_photo(request, pk):
    context = {}
    return render(request, "photos/edit_photo.html", context)
