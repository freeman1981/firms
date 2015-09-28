from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from datetime import datetime

from .models import Fire


def fires(request):
    return HttpResponse(serialize('geojson', Fire.objects.all()[:1000]), content_type='application/json')


class FireView(View):

    # TODO https://docs.djangoproject.com/en/1.8/ref/csrf/ need to read
    # def post(self, request, *args, **kwargs):
    #     return HttpResponse(serialize('geojson', Fire.objects.all()[:1000]), content_type='application/json')

    def get(self, request, *args, **kwargs):
        from_date = request.GET['from_date']
        from_date = datetime.strptime(from_date, '%m/%d/%Y')
        to_date = request.GET['to_date']
        to_date = datetime.strptime(to_date, '%m/%d/%Y')
        qs = Fire.objects.filter(date__lte=to_date, date__gte=from_date)
        return HttpResponse(serialize('geojson', qs), content_type='application/json')


class HomePageView(TemplateView):

    template_name = "fires/home.html"


class JQ(TemplateView):

    template_name = "fires/learn_js_jq.html"
