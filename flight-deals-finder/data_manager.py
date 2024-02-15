import requests
sheety_url = 'exccel sheet url that contains the lowest flight price'
class DataManager:
    def __init__(self,data):
        self.data = data
        self.response = requests.put(sheety_url, json=data)
        print(self.response.text)