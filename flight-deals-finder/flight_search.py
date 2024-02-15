import requests
import dateutil.relativedelta
from datetime import datetime
sheety_url = 'sheety co api'
class FlightSearch:

    def get_sheety_data(self):

        respond = requests.get(sheety_url)
        data = respond.json()
        return data

    def get_tequil_data(self,param, head):
        tequil_url = 'https://api.tequila.kiwi.com/locations/query'
        respond = requests.get(url=tequil_url, params=param, headers=head)
        return respond.json()

    def put_iatacode_sheety_data(self,data, json):

        respond = requests.put(f'{sheety_url}/{data}', json=json)
        return respond.text

    def searching_for_flights(self,apikey , fromcity , tocity, ):
        url = 'https://api.tequila.kiwi.com/v2/search'
        today_date = datetime.strftime(datetime.now().date(), "%d/%m/%Y")
        date_after_6_month = datetime.strftime(datetime.now().date() + dateutil.relativedelta.relativedelta(months=+6),
                                               "%d/%m/%Y")
        key_dict = {'apikey': 'tequila api-key',}
        param_dict = {
            'fly_from': fromcity,
            'date_from': today_date,
            'date_to': date_after_6_month,
            'fly_to': tocity
        }

        respond = requests.get(url=url, params=param_dict,headers=key_dict)
        return respond.json()
