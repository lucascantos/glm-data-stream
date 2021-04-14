
import netCDF4 as nc
import numpy as np
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

def fetch_glm_data(file_path):
    '''
    Retrieve data from netCDF data
    :params file_path: Path to netCDF file
    '''

    with open(file_path) as f:
        nc_file = nc.Dataset(file_path, 'r', keepweakref=True)
    
    glm_info = {
        'lon': {'var_name':'flash_lon'},
        'lat': {'var_name': 'flash_lat'},
        'area': {'var_name': 'flash_area'},
        'offset': {'var_name': 'flash_time_offset_of_first_event'},
    }

    array_func = lambda x: np.array(nc_file.variables[x][:])

    variable_names = [info['var_name'] for info in glm_info.values()]
    variable_data = [array_func(name) for name in variable_names]

    glm_data = zip(*variable_data)
    for single_data in glm_data:
        yield make_glm_object(single_data)

def make_glm_object(lightning_data):
    '''
    Make an lightning json object.
    :params lightning_data: Lightning data such as lat, lon area and datetime
    '''
    lat,lon,area,offset = lightning_data
    now = datetime.utcnow()
    offset = now.strftime("%Y%m%dT%H%M%S")
    return {
        'latitude': lat,
        'longitude': lon,
        'area': area,
        'datetime': datetime,
    }


