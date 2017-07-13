import random
import numpy as np
mylist = []
for i in range(20):
    a = random.randint(1, 100)
    mylist.append(a)

print (mylist)
print (len(mylist))

np.savetxt('randomlist.csv', mylist, delimiter=',')

loadedlist = np.loadtxt('randomlist.csv', delimiter=',')
print ("Contents of loadedlist as array object: " + str(loadedlist))

#print(type(loadedlist))
x = np.array(loadedlist).tolist()
#print(type(loadedlist))
print("Contents of loadedlist as list object: " + str(x))
