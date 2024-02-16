from django.urls import path, include

from petstagram.pets.views import delete_pet, details_pet, edit_pet, PetCreateView

urlpatterns = (
    path("create/", PetCreateView.as_view(), name="create pet"),
    path("<str:username>/pet/<slug:pet_slug>/",
         include([
             path("", details_pet, name="details pet"),
             path("edit/", edit_pet, name="edit pet"),
             path("delete/", delete_pet, name="delete pet"),
         ])
         )
)
