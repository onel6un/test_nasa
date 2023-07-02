from django.shortcuts import render

from .models import Slide


def index(request):
    template = 'main/index.html'
    slides = Slide.objects.all().order_by('order')
    context = {
        'slides': slides
    }
    return render(request, template, context)
