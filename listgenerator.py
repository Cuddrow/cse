from pylab import *

timelist = []

x = 0

for i in range(112):
    timelist.append(x)
    x = x+10

print (len(timelist))
print (timelist)

#This code saves the list in timefile.csv with no decimals.
savetxt("timefile.csv", timelist, fmt='%10.0f', delimiter=",")
