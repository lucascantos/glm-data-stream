
import netCDF4 as nc
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

def fetch_glm_data(nc_path):
    now = datetime.utcnow()
    with open(nc_path) as f:
        nc_file = nc.Dataset(nc_path, 'r', keepweakref=True)
    
    glm_info = {
        'lon': {'var_name':'flash_lon'},
        'lat': {'var_name': 'flash_lat'},
        'area': {'var_name': 'flash_area'},
        'offset': {'var_name': 'flash_time_offset_of_first_event'},
    }
    variable_names = [info['var_name'] for info in glm_info.values()]
    make_array = lambda x: np.array(nc_file.variables[x][:])
    variable_data = [make_array(name) for name in variable_names]
    glm_data = zip(*variable_data)
    for lat,lon,area,offset in glm_data:
        yield lat,lon,area,now.strftime("%Y%m%dT%H%M%S")

def make_glm_object(lat,lon,area,datetime):
    return json.dumps({
        'latitude': lat,
        'longitude': lon,
        'area': area,
        'datetime': datetime,
    }, default=str, sort_keys=False, allow_nan=True)


