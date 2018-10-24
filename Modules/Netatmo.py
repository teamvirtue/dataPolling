import requests
import time
import os
import datetime
import getToken

payload = {'grant_type': 'password',
           'username':'wotwot563@gmail.com',
           'password':'P@ssw0rd',
           'client_id':'5bc4769dae476315008ef0e0',
           'client_secret':'n6hDrLwFEyVHs0idQH1j7NF0iuo70u15kvctlJd',
           'scope': 'read_station'}
def function():
    try:
        response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
        response.raise_for_status()
        access_token=response.json()["access_token"]
        refresh_token=response.json()["refresh_token"]
        scope=response.json()["scope"]
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

    params = {
        'access_token': access_token,
    }

    try:
        response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
        response.raise_for_status()
        data = response.json()["body"]["devices"][0]["dashboard_data"]
        roomdata = {
                "room_name": "Livingroom",
                "last_humidity": data['Humidity'],
                "last_temperature": data['Temperature'],
                "last_amount_CO2": data['CO2'],
                "last_reading_time": datetime.datetime.utcfromtimestamp(data['time_utc']).strftime("%Y-%m-%d %H:%M:%S"),
                "nr_of_appliances": 100,
        }

        getToken.patchData('room/1',roomdata)
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)

    time.sleep(50)
def run():
    while 1:
        function()
