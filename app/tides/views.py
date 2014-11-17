from django.http import HttpResponse
import twilio.twiml
import tides.models
from .models import Tide
from datetime import date

def receive_sms(request):
    
    location = request.GET.get('Body', '').strip()
    print location

    sorted_locations = sorted(Tide.locations)

    if location == "Dublin":
	location = "Dublin (North Wall)"

    if location in sorted_locations:
        results =  Tide.objects.all().filter(location=location,date=date.today())
        if not results:
            tides.models.get_tides()
            results =  Tide.objects.all().filter(location=location,date=date.today())

        tide = results[0]

        message = "Tides for %s at location %s\nFirst Low: %s\nFirst High: %s\nSecond Low: %s\nSecond High: %s" % (
            date.today(), location, tide.first_low, tide.first_high, tide.second_low, tide.second_high)
    else:
        message = "Sorry, can't find tides for that location code. Available location codes are:\n"
        for location in sorted_locations:
            message += "%s,\n" % location

    resp = twilio.twiml.Response()
    resp.message(message)

    return HttpResponse(resp, content_type='text/xml')
