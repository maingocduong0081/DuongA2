#9.1
import math
x=int(input("nhập số:"))
def n(x):
 if x<0:
  return "-1"
 elif x>0:
  return "1"
 elif x==0:
  return "0"
a=n(x)
print(a)
