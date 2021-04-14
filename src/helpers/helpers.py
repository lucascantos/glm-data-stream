import json
def is_brazil(lat,lon):
    lat_bounds = [-35, 5]
    lon_bounds = [-75, -33]
    if lat in range(*lat_bounds) and lon in range(*lon_bounds):
        return True
    return False

def make_response(payload):
    return json.dumps({
        'lightnings': payload
    })