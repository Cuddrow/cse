import random
import numpy as np
mylist = []
for i in range(1026):
    kernel = random.randint(1,4)
    if kernel <5:
        kernel = "purple"
#    elif kernel >= 2:
#        kernel = "purple"
    mylist.append(kernel)

filename = 'cornkernels6.csv'

print (mylist)
print (len(mylist))
print (mylist.count("yellow"))
print (mylist.count("purple"))

np.savetxt(filename, mylist, delimiter=',', fmt="%s")


#print(type(loadedlist))
