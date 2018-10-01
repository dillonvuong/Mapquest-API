#Dillon Vuong 82352779 Project 3

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Uterr93mIe1sXG1AaJsa0MGWz9WNWmjf'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/'



def build_route_url(locations: list) ->str:
    '''
    This function takes a list of locations and returns a URL that
    represents the Open Directions Service.
    '''
    query_parameters = [
        ('key', MAPQUEST_API_KEY)]
    
    for location in locations:
        if location == locations[0]:
            query_parameters.append(('from', location))
        else:
            query_parameters.append(('to', location))

    return BASE_MAPQUEST_URL + 'directions/v2/route?' + urllib.parse.urlencode(query_parameters)

def build_elevation_urls(coordinates: list) -> list:
    '''
    This function takes a list of coordinates and returns a list of URLs that
    correspond to the coordinate in Map Quest Elevation API.
    '''
    url_list = []
    query_parameters = [
        ('key', MAPQUEST_API_KEY),
        ('unit', 'f'),
        ('latLngCollection','mutable')]
    for coordinate in coordinates:
        mutable = list(query_parameters[2])
        mutable[1] = ','.join(coordinate)
        query_parameters[2] = tuple(mutable)
        url_list.append(BASE_MAPQUEST_URL + 'elevation/v1/profile?' + urllib.parse.urlencode(query_parameters))
    return url_list

def get_results(urls: list) -> list:
    '''This function takes URLS and returns a Python dictionary representating the
       parsed JSON response for each URL.'''
    result = []
    for url in urls:
        result.append(get_result(url))
    return result

def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

def get_latlong(search_result:dict) -> list:
    'This function gets the coordinates and returns thme in a list to be processed.'
    result = []
    for coordinate in search_result['route']['locations']:
            result.append([str(coordinate['displayLatLng']['lat']),
                          str(coordinate['displayLatLng']['lng'])])
    return(result)


