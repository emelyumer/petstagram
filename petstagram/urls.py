from django.contrib import admin
from django.urls import path, include

from petstagram import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path("", include("petstagram.common.urls")),
    path("accounts/", include("petstagram.accounts.urls")),
    path("pets/", include("petstagram.pets.urls")),
    path("photos/", include("petstagram.photos.urls")),

    # Add a pattern that doesn't match any existing view
    path('nonexistent-page/', views.nonexistent_page, name='nonexistent_page'),
)
