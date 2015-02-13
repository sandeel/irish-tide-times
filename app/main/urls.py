from django.conf.urls import *
from django.contrib import admin
from tides import views
admin.autodiscover()

urlpatterns = patterns(
    (r'^admin/', include(admin.site.urls)),
    url('/?^$', views.LandingPageView.as_view(), name='index'),
    url(r'^receive_sms$', views.receive_sms, name="receive_sms"),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
