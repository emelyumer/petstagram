from django.shortcuts import render

# Callable
# - all functions
# - objects with overriden __call__ method


def signup_user(request):
    context = {}
    return render(request, "accounts/register-page.html", context)


def signin_user(request):
    pass


def signout_user(request):
    pass


def details_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass