import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
print(now + relativedelta(microseconds=19.05* 10**9))
x = [
    {'a', 1},
    {'b': 2}
]

y = [
    {'a', 1},
    {'b': 2}
]
x.extend(y)
y = set([0,1,2])
print([ for i in x])
x = list(set([i.items() for i in x]))