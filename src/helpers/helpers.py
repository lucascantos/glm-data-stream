
def make_response(payload):
    '''
    Make a JSON-String response
    '''
    import json
    return json.dumps({
        'lightnings': payload
    }, default=str, sort_keys=False, allow_nan=True)


def datetime_filter(timestamp, **kwargs):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    now = datetime.utcnow()
    lightning_date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        
    return now <= lightning_date+relativedelta(**kwargs)