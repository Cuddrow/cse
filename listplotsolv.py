from pylab import *

templist = loadtxt('./tempfile.csv', delimiter=',')
print ("templist type: " + str(type(templist)))
print(templist)
print (type(templist[0]))
timelist = loadtxt('./timefile.csv', delimiter=',', unpack=True)
print ("timelist type: " + str(type(timelist)))
print(timelist)
print (type(timelist[0]))

plot(timelist, templist)
axis([0,1200,0,25])
show()
