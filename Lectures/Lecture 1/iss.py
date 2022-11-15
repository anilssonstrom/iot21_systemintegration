import urllib.request
import json
import webbrowser


def get_position():
    # Hämta JSON-data, med koordinater
    # Parsa datan och hämta ut lat och long
    # Retur av lat, long
    api_url = 'http://api.open-notify.org/iss-now.json'

    # Hämta dokumentet
    response = urllib.request.urlopen(api_url)

    # Läsa dokumentet
    answer = response.read()
    json_dict = json.loads(answer)

    # Hämta specifik information
    latitude = json_dict['iss_position']['latitude']
    longitude = json_dict['iss_position']['longitude']

    return latitude, longitude


def open_map(latitude, longitude):
    # Använd variablerna för att skapa en URL
    url = f'https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}#map=3/{latitude}/{longitude}'

    # Öppna en webläsare med openstreetmap
    webbrowser.open_new_tab(url)


if __name__ == '__main__':
    lat, long = get_position()
    open_map(lat, long)
