import json
from src.services.s3 import S3
from src.services.sns import SNS
from src.helpers.helpers import datetime_filter
from src.helpers.helpers import is_brazil
from src.functions.glm_data import make_glm_object



def send_lightnings_sns(glm_data):
    '''
    Save recent lightnings to a buffer file
    :params glm_data: data loaded from GLM
    '''
    payload = []
    sns = SNS()
    for lightning_data in glm_data:
        coords = lightning_data['latitude'], lightning_data['longitude']
        if is_brazil(*coords):
            single_payload = make_glm_object(*lightning_data)
            payload.append(single_payload)
            if len(payload) >= 100:
                payload = []
                sns.send(json.dumps({'lightnings': payload}))
    if len(payload)>0:
        sns.send(json.dumps({'lightnings': payload}))
    return payload

def save_buffer(payload):
    '''
    Save recent lightnings to a buffer file
    :params payload: Lightning data sent to SNS
    '''
    s3 = S3()
    filepath = 'glm-buffer.json'
    try:
        buffer = s3.load(filepath)
    except:
        buffer = {'lightnings': []}
    buffer['lightnings'].extend(payload)
    unique_lightnings = {f"{lgt['latitude']}{lgt['longitude']}": lgt for lgt in buffer['lightnings']}
    recent_lightnings = filter(lambda x: datetime_filter(x['datetime'], minutes=10), unique_lightnings.values())
    s3.upload(
        json.dumps({'lightnings': list(recent_lightnings)},indent=4),
        filepath
        )
