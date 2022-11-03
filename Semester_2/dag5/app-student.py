# Opret API nøgle 
# -> Mit overblik -> Datadeling
# https://eloverblik.dk/

# API dokumentation
# https://api.eloverblik.dk/customerapi/index.html

# husk pip3 install requests
import requests
import json

# BE-IT 

# refresh_token er API nøgle oprettet på eloverblik.dk
refresh_token = 'xxx'

# får en data access token ved at kalde api med refresh_token
def get_token(user_token):
    get_data_access_token_url = 'https://api.eloverblik.dk/CustomerApi/api/token'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + user_token,
    }
    response = requests.get(get_data_access_token_url, headers=headers).json()
    print(response['result'])
    data_access_token_cache = response['result']
    return data_access_token_cache

# henter elmåler information med data access token
def get_meter(data_access):
    meter_point_url = 'https://api.eloverblik.dk/CustomerApi/api/meteringpoints/meteringpoints'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + data_access,
    }
    meters = requests.get(meter_point_url, headers=headers)

    first_meter = meters.json()['result'][0]['meteringPointId']
    print('Meter id is: ' + str(first_meter))
    return first_meter

# henter elmåler data med data access token
def get_data(data_access):
    time_series = 'https://api.eloverblik.dk/customerapi/api/meterdata/gettimeseries/2022-03-01/2022-09-01/Hour'

    meter_data = 'https://api.eloverblik.dk/CustomerApi/api/meterdata/gettimeseries/'

    timeseries_data = {
        'dateFrom': str('2022-03-01'),
        'dateTo': str('2022-09-01'),
        'aggregation': 'Day'
    }

    meter_data_url = meter_data + timeseries_data['dateFrom'] + '/' + timeseries_data['dateTo'] + '/' + timeseries_data['aggregation']

    # indsæt meter id fra API her
    first_meter_cache = 'xx'

    meter_json = {
        "meteringPoints": {
            "meteringPoint": [
                first_meter_cache
            ]
        }
    }

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + data_access,
    }

    meter_data_request = requests.post(meter_data_url, headers=headers, json=meter_json)
    json_data = meter_data_request.json()

    with open('meter_data.json', 'w') as f2:
        json.dump(json_data, f2)

# henter elpriser fra energidataservice
# https://api.energidataservice.dk/

def elspotpriser():
    url = 'https://api.energidataservice.dk/dataset/Elspotprices?offset=0&sort=HourUTC%20DESC&timezone=dk'
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers).json()
    print(response)
    with open('price_data.json', 'w') as f:
        json.dump(response, f)

def ladestandere():
    url2 = 'https://clever-app-prod.firebaseio.com/prod/locations/V1.json'
    url3 = 'https://clever-app-prod.firebaseio.com/prod/availability/V1.json'
    url4 = 'https://clever-app-prod.firebaseio.com/chargers/v2/availability.json'
    url5 = 'https://clever-app-prod.firebaseio.com/chargers/v3/locations.json'
    headers = {"Content-Type": "application/json"}

    response = requests.get(url2, headers=headers).json()
    print(response)

# kalder funktioner med parametre
#data_access = get_token(refresh_token)
#meter_id = get_meter(data_access)
#get_data(data_access)
elspotpriser()
#ladestandere()