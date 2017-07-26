import numpy as np
#np.savetxt('randomlist.csv', mylist, delimiter=',')
regularlist = []
loadedlist = np.loadtxt('./temp_file_store/temparray31jan.csv', delimiter=',')
print ("Contents of loadedlist as array object: " + str(loadedlist))
print ("Object type for loadedlist is " + str(type(loadedlist)) + " Length is " + str(loadedlist.size))

#print(type(loadedlist))
#x = np.array(loadedlist).tolist()
#print(type(loadedlist))
#print("Contents of loadedlist as list object: " + str(x))

listsum = sum(loadedlist)
meantemp = listsum/(loadedlist.size)
print("Mean temperature %s C" % (meantemp))
