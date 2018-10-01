#Dillon Vuong 82352779 Project 3

#Consumer Key	Uterr93mIe1sXG1AaJsa0MGWz9WNWmjf
#Consumer Secret	fc2wxGhvhQwyAdvd

import mapquest
import mapquest_classes


def _iterate(iterations: int) -> list:
    '''Takes an integer and runs _read_input() that many times and
     returns a list of the inputs.'''
    directions = []
    for x in range(iterations):
        directions.append(input())
    return directions

def _perform_outputs(outputs: 'list of outputs') -> None:
    '''Performs the given outputs in the order in which they are given'''
    try:
        print()
        for output in outputs:
            getattr(mapquest_classes, output)().run(result)
            print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    except KeyError:
        print()
        print('NO ROUTE FOUND')
    except:
        print()
        print('MAPQUEST ERROR')
        

    

        
if __name__ == '__main__':
    
    number_of_locations = int(input())
    locations = _iterate(number_of_locations)

    number_of_outputs = int(input())
    outputs = _iterate(number_of_outputs)

    route_url = mapquest.build_route_url(locations)
    result = mapquest.get_result(route_url)
    _perform_outputs(outputs)
