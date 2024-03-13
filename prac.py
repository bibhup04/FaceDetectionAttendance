import os
from time import strftime
from datetime import datetime




now=datetime.now()
d1=now.strftime("%d/%m/%Y")
dtString=now.strftime("%H:%M:%S")
day=now.strftime("%d")

d2='14/04/2023'

print(d1)
print(dtString)
print('new')
#print(d1 - now.strftime("%d-1/%m-2/%Y-5"))
print(day)
print(int(day)+5)
print( d1 == d2)

mi=int(now.strftime("%M"))
min=(40+40)%60
hou=(int(now.strftime("%H"))+((40+40)//60))
print(hou,":",min)