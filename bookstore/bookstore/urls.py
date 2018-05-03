from django.contrib import admin
from django.conf.urls import url, include
from store import urls as store_urls

urlpatterns = [
    url(r'^store', include(store_urls), name='store'),
    url(r'^accounts', include('registration.backends.default.urls')),
    url(r'^admin$', admin.site.urls),
]
