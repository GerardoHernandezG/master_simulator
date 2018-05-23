from django.conf.urls import include, url

urlpatterns = [
    url(r'^simulator/', include(('simulator.urls'), namespace='simulator')),
]
