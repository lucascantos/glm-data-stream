import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
print(now + relativedelta(microseconds=19.05* 10**9))

x = np.array([0,1,2])
y = np.array([0,1,2])
z = np.array([2,3,3])
a = [x,y,z]
b = zip(*a)
for i in b:
    print(i)
# a = 10 in range(10)
# print(a)

# x = [0,1,2,3,4]
# *a,_,_ = x
# print(a)