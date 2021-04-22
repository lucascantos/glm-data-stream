import json
from src.helpers.helpers import make_response
from src.functions.lightning_stream import WeatherLightnings
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

    lightnings = WeatherLightnings()
    glm_data = fetch_glm_data(file_path)   
    
    lightnings.send_lightnings_sns(glm_data)
    # lightnings.save_buffer()

def glm_buffer(event=None, context=None):
    '''
    Grab lightnings within a date range
    '''
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    end_date = datetime(2021,1,1,12)
    ini_date = end_date - relativedelta(minutes=5)

    lightnings = WeatherLightnings()
    s3 = ''
    deltatime = (end_date - ini_date).total_seconds()
    for i in range(0, int(deltatime), 20):
        file_datetime = ini_date+relativedelta(seconds=i)
        file_timestamp = file_datetime.strftime('%Y%j%H%M')
        latest_file = s3.latest_file(f"OR_GLM-L2-LCFA_G16_s{file_timestamp}")
        glm_data = fetch_glm_data(latest_file)
        lightnings.payload.append(glm_data)

    payload = lightnings.brazilian_lightnings()
    make_response(list(payload))