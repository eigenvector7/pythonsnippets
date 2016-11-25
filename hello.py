#!/usr/bin/env python3
from datetime import datetime

print("Hello World - trying out git from within PyCharm CE")

hour = datetime.now().hour

if hour < 12:
    print("Good Morning, it's {0} o'clock".format(hour))
elif hour == 12:
    print("Good Noon, it's exactly {0} o'clock".format(hour))
else:
    print("Good Evening it's {} o'clock".format(hour))



