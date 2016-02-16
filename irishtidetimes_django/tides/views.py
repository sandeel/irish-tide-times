from django.http import HttpResponse
import twilio.twiml
import tides.models
from .models import Tide
from datetime import date
from django.views import generic
from django.core import serializers
import datetime

class LandingPageView(generic.TemplateView):
    """"""
    template_name = 'website/landing_page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(generic.TemplateView, self).get_context_data(**kwargs)
        results =  tides.models.get_tides()
        context['results'] = results
        context['date'] = datetime.datetime.now().date
        return context

def receive_sms(request):

    location = request.GET.get('Body', '').strip()

    sorted_locations = sorted(Tide.locations)

    if location.lower() == "dublin":
        location = "Dublin (North Wall)"

    if location.lower() in ([x.lower() for x in sorted_locations]):
        results =  tides.models.get_tides().filter(location=location,date=date.today())

        tide = results[0]

        message = "Tides for %s at location %s\nFirst Low: %s:%s\nFirst High: %s:%s\nSecond Low: %s:%s\nSecond High: %s:%s" % (
            date.today(),
            location,
            str(tide.first_low.hour).zfill(2),
            str(tide.first_low.minute).zfill(2),
            str(tide.first_high.hour).zfill(2),
            str(tide.first_high.minute).zfill(2),
            str(tide.second_low.hour).zfill(2),
            str(tide.second_low.minute).zfill(2),
            str(tide.second_high.hour).zfill(2),
            str(tide.second_high.minute).zfill(2),
            )
    else:
        message = "Sorry, can't find tides for that location code. Available location codes are:\n"
        for location in sorted_locations:
            message += "%s,\n" % location

    resp = twilio.twiml.Response()
    resp.message(message)

    return HttpResponse(resp, content_type='text/xml')

def tides_as_json(request):
    data = serializers.serialize("json", tides.models.get_tides())
    return HttpResponse(data, content_type='text/json')
