import json
from src.helpers.helpers import make_response
from src.functions.lightning_stream import WeatherLightnings
from src.functions.glm_data import Glm  

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
    glm = Glm()
    glm_data = glm.fetch_glm_data(file_path)   
    
    lightnings.send_lightnings_sns(glm_data)
    # lightnings.save_buffer()

def glm_buffer(event=None, context=None):
    '''
    Grab lightnings within a date range
    '''
    print(event)
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    lightnings = WeatherLightnings()
    glm = Glm()

    end_date = datetime.utcnow().replace(second=40)
    ini_date = end_date - relativedelta(minutes=5)
    product_name = "GLM-L2-LCFA"
    filepath = f"{product_name}/%Y/%j/%H/OR_{product_name}_G16_s%Y%j%H%M%S"
    deltatime = (end_date - ini_date).total_seconds()
    for i in range(0, int(deltatime), 20):
        file_datetime = ini_date+relativedelta(seconds=i)
        file_timestamp = file_datetime.strftime(filepath)
        latest_file = glm.bucket.latest_file(file_timestamp)
        print(latest_file)
        if not latest_file:
            continue
        glm_data = glm.fetch_glm_data(latest_file)
        lightnings.payload.extend(list(glm_data))

    payload = lightnings.brazilian_lightnings()
    return make_response(list(payload))