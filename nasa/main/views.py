from django.http import HttpResponse


def index(request):
    return HttpResponse('Vse_ok')