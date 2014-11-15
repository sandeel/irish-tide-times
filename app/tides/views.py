from django.http import HttpResponse
import twilio.twiml

def receive_sms(request):

    """Respond and greet the caller by name."""
 
    message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(request.GET.get('Body', ''))

    return HttpResponse(resp, content_type='text/xml')
