from django.db import models
from bs4 import BeautifulSoup
import requests
from datetime import date


class Tide(models.Model):

    date = models.DateField()
    location = models.CharField(max_length=20)
    first_low= models.TimeField()
    first_high= models.TimeField()
    second_low= models.TimeField()
    second_high= models.TimeField()

def get_tides():
        
    url = "http://www.irishtimes.com/weather/tides"

    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data)

    locations = {
                    "Arklow",
                    "Bantry",
                    "Wexford",
    }

    for td in soup.find_all('td'):
        if td.getText() in locations:
            tr = td.parent
            tds = tr.find_all('td')
            location = tds[0].text
            first_low = tds[1].text
            first_high = tds[2].text
            second_low = tds[3].text
            second_high = tds[4].text

            tide = Tide()
            tide.date = date.today()
            tide.location = location
            tide.first_low = first_low
            tide.first_high = first_high
            tide.second_low = second_low
            tide.second_high = second_high

            tide.save()
