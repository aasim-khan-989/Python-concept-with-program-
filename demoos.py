import os

print(os.getcwd())
os.chdir("E:\\Aasim college\python")
print(os.getcwd())
os.chdir("E:\\Aasim college\python\\python program")
print(os.getcwd())

from datetime import date

x = date(2021,12,22)
print(x)

from datetime import time

x = time(12,30,40)
print(x)

from datetime import datetime

x = datetime.now()
print(x)

from datetime import timedelta

x = datetime.now()
y = x + timedelta(days = 3)
print(y)

import sys
print(sys.version)
print(sys.platform)
print(sys.path)