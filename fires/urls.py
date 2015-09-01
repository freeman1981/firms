from django.conf.urls import url
from .views import fires

urlpatterns = [
    url(r'^$', fires),
]
