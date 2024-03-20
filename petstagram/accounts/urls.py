from django.urls import path, include

from petstagram.accounts.views import SignUpUserView, SignInUserView, ProfileDetailView, edit_profile, delete_profile, signout_user

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),

    path("profile/<int:pk>/", include([
        path("", ProfileDetailView.as_view(), name="details profile"),
        path("edit/", edit_profile, name="edit profile"),
        path("delete/", delete_profile, name="delete profile"),
        ]),
    )
)
