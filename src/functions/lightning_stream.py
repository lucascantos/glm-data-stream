import json
from src.services.s3 import S3
from src.services.sns import SNS
from src.helpers.helpers import datetime_filter
from src.functions.glm_data import make_glm_object

class WeatherLightnings:
    def __init__(self):
        self.sns = SNS()
        self.s3 = S3()
        self.filepath = 'glm-buffer.json'
        self.payload=[]

    def send_lightnings_sns(self, glm_data):
        '''
        Save recent lightnings to a buffer file
        :params glm_data: data loaded from GLM
        '''
        payload = []
        for lightning_data in glm_data:
            coords = lightning_data['latitude'], lightning_data['longitude']
            if self.is_brazil(*coords):
                single_payload = make_glm_object(*lightning_data)
                payload.append(single_payload)
                if len(payload) >= 100:
                    payload = []
                    self.sns.send(json.dumps({'lightnings': payload}))
        if len(payload)>0:
            self.sns.send(json.dumps({'lightnings': payload}))
        self.payload.extend(payload)

    @classmethod
    def is_brazil(cls,lat,lon):
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

    def save_buffer(self):
        '''
        Save recent lightnings to a buffer file
        :params payload: Lightning data sent to SNS
        '''
        try:
            buffer = s3.load(self.filepath)
        except:
            buffer = {'lightnings': []}
        buffer['lightnings'].extend(self.payload)
        unique_lightnings = {f"{lgt['latitude']}{lgt['longitude']}": lgt for lgt in buffer['lightnings']}
        recent_lightnings = filter(lambda x: datetime_filter(x['datetime'], minutes=10), unique_lightnings.values())
        self.s3.upload(
            json.dumps({'lightnings': list(recent_lightnings)},indent=4),
            self.filepath
            )
