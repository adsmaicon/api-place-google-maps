import googlemaps
import pprint
import time

# Define the API Key.
API_KEY = 'CHAVE DE API'

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)

geocode_result = gmaps.geocode('Rua David Tows, Curitiba, Parana')

location = geocode_result[0].get('geometry').get('location')

# in lat/lon format, along with a radius measured in meters
# https://developers.google.com/maps/documentation/places/web-service/supported_types#table1
places_result  = gmaps.places_nearby(location=f'{location.get("lat")},{location.get("lng")}', radius = 40000, open_now =False , type = 'restaurant')

time.sleep(3)

place_result  = gmaps.places_nearby(page_token = places_result['next_page_token'])
stored_results = []

for place in places_result['results']:

    # define the place id, needed to get place details. Formatted as a string.
    my_place_id = place['place_id']

    # define the fields you would liked return. Formatted as a list.
    my_fields = ['name','formatted_phone_number','website']

    # make a request for the details.
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

    # print the results of the details, returned as a dictionary.
    pprint.pprint(places_details['result'])

    # store the results in a list object.
    stored_results.append(places_details['result'])
