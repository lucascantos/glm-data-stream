import json
def is_brazil(lat,lon):
    '''
    Checks if the given coordinate is inside Brazil's Bounding Box
    :params lat: latitude
    :params lon: longitude
    '''
    lat_bounds = [-35, 5]
    lon_bounds = [-75, -33]
    if lat in range(*lat_bounds) and lon in range(*lon_bounds):
        return True
    return False

def make_response(payload):
    '''
    Make a JSON-String response
    '''
    return json.dumps({
        'lightnings': payload
    }, default=str, sort_keys=False, allow_nan=True)