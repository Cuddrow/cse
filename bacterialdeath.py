from pylab import *

dt = 20
initial_pop = 9*(10**10)
D = 0.3
generations = 40

timearray = zeros(generations)
bactarray = zeros(generations)
bactarray[0] = initial_pop
print(bactarray)

for n in range(1, generations):
    timearray[n] = timearray[n-1]+dt
    bactarray[n] = bactarray[n-1]-bactarray[n-1]*D

print (timearray)
print (bactarray)

plot(timearray, bactarray)
yscale('log')
show()
