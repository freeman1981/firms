from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Fire


def fires(request):
    return HttpResponse(serialize('geojson', Fire.objects.all()[:1000]), content_type='application/json')


class HomePageView(TemplateView):

    template_name = "fires/home.html"

