from django.conf.urls import url
from . import views
app_name = 'simulator'

urlpatterns = [
    #simulator
    url(r'^index/', views.index),
]
