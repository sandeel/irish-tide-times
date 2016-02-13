from django.conf.urls import *
from django.contrib import admin
from tides import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^receive_sms/', views.receive_sms, name="receive_sms"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.LandingPageView.as_view(), name='index'),
    url(r'^api/v1/ireland$', views.tides_as_json, name='tides_as_json'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
