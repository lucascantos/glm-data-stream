
import netCDF4 as nc
import numpy as np
import json
import io
from src.services.s3 import S3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.configs.configs import GOES16_BUCKET

class Glm:
    def __init__(self):
        self.bucket = S3(GOES16_BUCKET)
    
    def fetch_glm_data(self, file_path):
        '''
        Retrieve data from netCDF data
        :params file_path: Path to netCDF file
        '''
        if 'sample' in file_path.split('/'):
            with open(file_path) as f:
                nc_file = nc.Dataset(file_path, 'r', keepweakref=True)
        else:
            nc_file = self.bucket.load(file_path)
            nc_file = nc.Dataset('irrelevant_name', memory=nc_file)
        
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
            yield self.make_glm_object(single_data)

    def make_glm_object(self, lightning_data):
        '''
        Make an lightning json object.
        :params lightning_data: Lightning data such as lat, lon area and datetime
        '''
        lon,lat,area,offset = lightning_data
        now = datetime.utcnow()
        offset = now.strftime("%Y-%m-%dT%H:%M:%S")
        return {
            'latitude': float(round(lat,5)),
            'longitude': float(round(lon,5)),
            'area': float(area),
            'datetime': offset,
    }


