from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'', include('website.urls')),
    (r'', include('tides.urls')),
    (r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
