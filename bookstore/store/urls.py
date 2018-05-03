import xml.etree.ElementInclude
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', xml.etree.ElementInclude.include('views.store')),
]
