
def make_response(payload):
    '''
    Make a JSON-String response
    :params payload: list of lightning events
    '''
    import json
    return {
        'statusCode': 200,
        'body': json.dumps({
            'lightnings': payload
        })
    }

def datetime_filter(timestamp, **kwargs):
    '''
    Filter data based on date time 
    :params timestamp: string with timestamp format
    :params **kwargs: Arguments for relativedelta function, from dateutils
    '''
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    now = datetime.utcnow()
    lightning_date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        
    return now <= lightning_date+relativedelta(**kwargs)