from django.conf.urls import patterns, url

from tides import views

urlpatterns = patterns(
    'tides.views',
    url(r'^receive_sms$', views.receive_sms, name="receive_sms"),
)
