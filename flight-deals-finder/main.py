#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from pprint import pprint
import smtplib

sheet_data = FlightSearch().get_sheety_data()

for i in range(9):
    data = FlightSearch().searching_for_flights(apikey='your key', tocity=sheet_data['prices'][i]['iataCode'],fromcity='EG')
    if sheet_data['prices'][i]['lowestPrice'] < data['data'][0]['price']:
        my_email = 'email' # gmail
        password = 'project password'
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs='email to send to',
                                msg=f"Subject:Found a good flight deal\n\nTfrom {data['data'][0]['cityFrom']} to {data['data'][0]['cityTo']} price: €{data['data'][0]['price']}")
        print(f"")
