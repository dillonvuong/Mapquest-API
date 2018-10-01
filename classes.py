def lat_long(search_result: dict) -> list:
    '''This function returns the latitude and logitudes of the locations
       in a list.'''
    result = []
    for coordinate in search_result['route']['locations']:
        result.append((coordinate['displayLatLng']['lat'],
                       coordinate['displayLatLng']['lng']))
    return result

def steps(search_result: dict) -> list:
    '''This function returns the direction to each location in a list.'''
    result = []
    for step in search_result['route']['legs'][0]['maneuvers']:
        result.append(step['narrative'])
    return result

def total_time(search_result: dict) -> str:
    '''This function returns the total time.'''
    h, m, s = search_result['route']['formattedTime'].split(':')
    
    minutes = int(h) * 60 + int(m) + int(s)/60
    return str(round(minutes)) + ' minutes'

def total_distance(search_result: dict) -> int:
    '''This function returns the total distance.'''
    return str(round(search_result['route']['distance'])) + ' miles'

def elevation(search_result: dict) -> list:
    '''This function returns the elevation of all locations in a list'''
    result = []
    for profile in search_result['elevationProfile']:
        result.append(round(profile['height']))
    return result
    
