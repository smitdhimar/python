#module platform

import platform

print(platform.system())
print(platform.architecture())
print(platform.processor())
print(platform.release())
print(platform.machine())
# print(dir(platform))

#module datetime
import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().date())
print(datetime.datetime.now().day)
print(datetime.datetime.now().isocalendar())
print(datetime.MAXYEAR(2023))
#this are the example of datetime object
#but but but, there is lot more apart from these things there are formats for printing dates such as %A,%B for different purposes.No need to go in the deep things just look for documentation 