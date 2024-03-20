from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm
from petstagram.accounts.models import Profile


# Callable
# - all functions
# - objects with overriden __call__ method



class SignInUserView(auth_views.LoginView):
    template_name = "accounts/signin-user.html"


class SignUpUserView(views.CreateView):
    template_name = "accounts/signup_user.html"
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # form_valid going to call 'save'
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "accounts/details_profile.html"


def edit_profile(request, pk):
    context = {}
    return render(request, "accounts/edit_profile.html", context)


def delete_profile(request, pk):
    context = {}
    return render(request, "accounts/delete_profile.html", context)
