import json
from src.functions.lightning_stream import save_buffer
from src.functions.lightning_stream import send_lightnings_sns
from src.functions.glm_data import fetch_glm_data  

def glm_data(event=None, context=None):
    '''
    Opens lightning data from GLM and send it to a SNS
    '''
    print(event)
    file_path = event['path']
    glm_data = fetch_glm_data(file_path)
    payload = send_lightnings_sns(glm_data)    
    save_buffer(payload)

