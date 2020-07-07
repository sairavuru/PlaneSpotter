##Libraries
import numpy as np
import pandas as pd
import requests, json, argparse

argparser = argparse.ArgumentParser(
    description='grab flight data from latitude/longitude')

argparser.add_argument(
    '-ll',
    '--latlong',
    help='latitude and longitude of search center [i.e. 36.0828, -115.1375]')

argparser.add_argument(
    '-ap',
    '--airport',
    help='airport ICAO code [i.e. KLAS]')

argparser.add_argument(
    '-r',
    '--range',
    help='range(miles) to search')

argparser.add_argument(
    '-a',
    '--airline',
    help='airline code')

#def _main_(args):
def _main_(airline, airport, landing):
    # print(args)
    # lat = float(args.latlong.split(',')[0])
    # long = float(args.latlong.split(',')[1])
    # range = float(args.range)
    # airline = str(args.airline)
    # airport = str(args.airport)

    if airline == 'american':
        airline_code = 'AA'
    elif airline == 'delta':
        airline_code = 'DL'
    elif airline == 'spirit':
        airline_code = 'NK'
    elif airline == 'allegiant':
        airline_code = 'G4'
    elif airline == 'united':
        airline_code = 'UA'
    elif airline == 'alaska':
        airline_code = 'AS'
    elif airline == 'jetblue':
        airline_code = 'B6'
    elif airline == 'southwest':
        airline_code = 'WN'
    elif airline == 'hawaiian':
        airline_code = 'HA'
    elif airline == 'frontier':
        airline_code = 'F9'

    #aviationstack method
    #URL; http://api.aviationstack.com/v1/flights?access_key=<API key>&dep_iata=<>&airline_iata=<>
    apiKey = ""
    url = "http://api.aviationstack.com/v1/flights?access_key="+str(apiKey)

    if landing == 0:
        payload = {'dep_icao':airport, 'airline_iata': airline_code, 'flight_data':'active'}
    else:
        payload = {'arr_icao': airport, 'airline_iata': airline_code, 'flight_data': 'active'}
    response = requests.get(url, params=payload)

    if response.status_code == 200:
        #print(response.json())
        test = json.loads(response.text)
    else:
        print("Error executing request")


    # for i in test['data']:
    #     try:
    #         flight = i['flight']['iata']
    #     except:
    #         flight = 'N/A'
    #
    #     try:
    #         tail = i['aircraft']['registration']
    #     except:
    #         tail = 'N/A'
    #
    #     try:
    #         orig = i['departure']['icao']
    #     except:
    #         orig = 'N/A'
    #
    #     try:
    #         dest = i['arrival']['icao']
    #     except:
    #         dest = 'N/A'

    try:
        flight = test['data'][0]['flight']['iata']
    except:
        flight = 'N/A'

    try:
        tail = test['data'][0]['aircraft']['registration']
    except:
        tail = 'N/A'

    try:
        orig = test['data'][0]['departure']['icao']
    except:
        orig = 'N/A'

    try:
        dest = test['data'][0]['arrival']['icao']
    except:
        dest = 'N/A'

    #print(flight, tail, orig, dest)

    return flight, tail, orig, dest

# if __name__ == '__main__':
#     #args = argparser.parse_args()
#     #flight, tail, orig, dest = _main_(args)
#     airline = 'allegiant'
#     airport = 'KLAS'
#     flight, tail, orig, dest = _main_(airline, airport)
#     print(flight, tail, orig, dest)