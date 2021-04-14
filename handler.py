import json
from src.functions.glm_data import fetch_glm_data
from src.functions.glm_data import make_glm_object
from src.helpers.helpers import is_brazil    
from src.helpers.helpers import make_response    

def glm_data(event=None, context=None):
    print(event)

    file_path = event['path']
    glm_data = fetch_glm_data(file_path)
    payload = []
    for lightning_data in glm_data:
        lat,lon,*_ = lightning_data
        if is_brazil(lat,lon):
            single_payload = make_glm_object(*lightning_data)
            payload.append(single_payload)
    return make_response(payload)
    
    # update buffer file. New file every 5min
    # send info to Websocket

