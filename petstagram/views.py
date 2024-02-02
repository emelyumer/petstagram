from django.http import HttpResponseNotFound
from django.template.loader import render_to_string


def nonexistent_page(request):
    return HttpResponseNotFound(render_to_string('404.html'))
