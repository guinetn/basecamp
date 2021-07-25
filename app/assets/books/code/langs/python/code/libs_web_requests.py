see FAST API 

## urllib

import json
import urllib.request

def chunks(data, rows=10000):
    """ Divides the data into 10000 rows each """

    for i in range(0, len(data), rows):
        yield data[i:i+rows]

url_mag="https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json"
url_plasma="https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"
# url_plasma="https://services.swpc.noaa.gov/json/goes/primary/xray-plasmas-7-day.json"

mag=urllib.request.urlopen(url_mag)
plasma=urllib.request.urlopen(url_plasma)

mag_json=json.loads(mag.read())
plasma_json=json.loads(plasma.read())

mag_json[0:2]

plasma_json[0:2]
