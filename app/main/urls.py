from django.contrib.auth.decorators import login_required

from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns(
    'main.views',
    url(r'^$', views.landing, name="landing_page"),
)
