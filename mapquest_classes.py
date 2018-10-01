#Dillon Vuong 82352779 Project 3
import mapquest
class LATLONG():
    def run(self, search_result: dict) -> str:
        '''This function returns the latitude and logitudes of the locations.'''
        if len(search_result['route']) > 1:
            print('LATLONGS')    
        for coordinate in search_result['route']['locations']:
            lat = round(coordinate['displayLatLng']['lat'],2)
            lng = round(coordinate['displayLatLng']['lng'],2)
            if lat > 0:
                lat = str(lat) + 'N'
            else:
                lat = str(lat*(-1)) + 'S'
      
            if lng > 0:
                lng = str(lng) + 'E'
            else:
                lng = str(lng*(-1)) + 'W'
                
            print(lat,lng)

class STEPS():
    def run(self, search_result: dict) -> str:
        '''This function returns the direction to each location.'''
        if len(search_result['route']) > 1:
            print('DIRECTIONS')  
        for index in range(len(search_result['route']['legs'])):
            for step in search_result['route']['legs'][index]['maneuvers']:
                print(step['narrative'])
       

class TOTALTIME():
    def run(self, search_result: dict) -> str:
        '''This function returns the total time.'''
        h, m, s = search_result['route']['formattedTime'].split(':')
        
        minutes = int(h) * 60 + int(m) + int(s)/60
        print('TOTAL TIME: ' + str(round(minutes)) + ' minutes')

class TOTALDISTANCE():
    def run(self, search_result: dict) -> str:
        '''This function returns the total distance.'''
        print('TOTAL DISTANCE: ' + str(round(search_result['route']['distance'])) + ' miles')

class ELEVATION():
    def run(self, search_result: dict) -> str:
        '''This function returns the elevation of all locations'''
        elevation_search_result = mapquest.get_results(mapquest.build_elevation_urls(mapquest.get_latlong(search_result)))
        if len(search_result['route']) > 1:
            print('ELEVATIONS')
        for index in range(len(elevation_search_result)):
            for profile in elevation_search_result[index]['elevationProfile']:
                print(round(profile['height']))

