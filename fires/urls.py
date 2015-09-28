from django.conf.urls import url
from .views import fires, FireView

urlpatterns = [
    url(r'^$', FireView.as_view()),
]
