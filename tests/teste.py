
def glm_buffer(event=None, context=None):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    end_date = datetime(2021,1,1,12)
    ini_date = end_date - relativedelta(minutes=4)

    deltatime = (end_date - ini_date).total_seconds()
    for i in range(0, int(deltatime), 20):
        filename = ini_date+relativedelta(seconds=i)
        yield filename

import itertools
x = glm_buffer()
payload = True

while payload:=list(itertools.islice(x,5)):
    print(payload)

