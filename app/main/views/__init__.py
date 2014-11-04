import logging

from django.core.urlresolvers import reverse

from django.views import generic


class HomePageView(generic.TemplateView):
    """"""
    template_name = 'main/home.html'

home = HomePageView.as_view()


class LandingPageView(generic.TemplateView):
    """"""
    template_name = 'main/landing_page.html'

landing = LandingPageView.as_view()
