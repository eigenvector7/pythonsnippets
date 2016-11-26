#!/usr/bin/env python3
from datetime import datetime
from collections import deque
import time
import random


print("Hello World - trying out git from within PyCharm CE")

hour = datetime.now().hour

minuteQ = deque()
minuteL = list()

# Compare time difference between deque vs list operations
#TODO - profile using CPU time
numIterations = 100000

starttime = time.time()
for i in range(numIterations):
#    idx = random.randrange(0,numIterations)
    minuteL.insert(0,i)
lTimeDelta = time.time()-starttime
print("List time {} ".format(lTimeDelta))

starttime = time.time()
for i in range(numIterations):
#    idx = random.randrange(0,numIterations)
    minuteQ.appendleft(i)
qTimeDelta = time.time()-starttime
print("Q time {} ".format(qTimeDelta))

print("Insert left in dequeue is {} times faster".format(round(lTimeDelta/qTimeDelta)))




if hour < 12:
    print("Good Morning, it's {0} o'clock".format(hour))
elif hour == 12:
    print("Good Noon, it's exactly {0} o'clock".format(hour))
else:
    print("Good Evening it's {} o'clock".format(hour))





