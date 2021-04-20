import json
from src.functions.lightning_stream import save_buffer
from src.functions.lightning_stream import send_lightnings_sns
from src.functions.glm_data import fetch_glm_data  

def glm_data(event=None, context=None):
    '''
    Opens lightning data from GLM and send it to a SNS
    '''
    message = json.loads(event['Records'][0]['Sns']['Message'])
    file_path = message['Records'][0]['s3']['object']['key']
    product_name = file_path.split('/')[0]
    if product_name != 'GLM-L2-LCFA':
        return
    print(event)
    glm_data = fetch_glm_data(file_path)
    payload = send_lightnings_sns(glm_data)    
    save_buffer(payload)