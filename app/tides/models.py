from django.db import models
from bs4 import BeautifulSoup
import requests
from datetime import date


class Tide(models.Model):

    def __str__(self):
        return self.location + " - " + self.date.strftime("%B %d, %Y")

    date = models.DateField()
    location = models.CharField(max_length=20)
    first_low= models.TimeField(null=True)
    first_high= models.TimeField(null=True)
    second_low= models.TimeField(null=True)
    second_high= models.TimeField(null=True)

    locations = {
            "Dublin (North Wall)",
            "Arklow",
            "Bantry",
            "Belfast",
            "Castletownbere",
            "Cobh",
            "Derry",
            "Dingle",
            "Dungarvan",
            "Dun Laoghaire",
            "Galway",
            "Greystones",
            "Howth",
            "Kilkeel",
            "Killybegs",
            "Kinsale",
            "Larne",
            "Limerick Docks",
            "Moville",
            "Portrush",
            "Rathmullen",
            "Schull",
            "Sligo",
            "Warrenpoint",
            "Waterford Bridge",
            "Westport",
            "Wexford",
            "Wicklow",
            "Youghal",
    }



def get_tides():
        
    url = "http://www.irishtimes.com/weather/tides"

    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data)

    for td in soup.find_all('td'):
        if td.getText() in Tide.locations:
            tr = td.parent
            tds = tr.find_all('td')

            location = tds[0].text

            first_low = tds[1].text
            first_high = tds[2].text
            second_low = tds[3].text
            second_high = tds[4].text

            results =  Tide.objects.all().filter(location=location,date=date.today())
            if not results.exists():
                tide = Tide()
                tide.date = date.today()
                tide.location = location.lower()

                if first_low:
                    tide.first_low = first_low 
                else:
                    tide.first_low = None

                if first_high:
                    tide.first_high = first_high 
                else:
                    tide.first_high = None

                if second_low:
                    tide.second_low = second_low 
                else:
                    tide.second_low = None

                if second_high:
                    tide.second_high = second_high 
                else:
                    tide.second_high = None

                print("Saving tide for ",location,"... :)")
                tide.save()
            else:
                print("Already have tide for ",location," today... :)")

