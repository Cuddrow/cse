import pandas

corncob = pandas.read_csv('cornkernels1.csv', names=['color'])
corncob = (list(corncob['color']))
print ("Contents of loadedlist: " + str(corncob))
print(corncob)

#print(type(corncob))
#print(len(corncob))
#print("Amount of yellow kernels: " + str(corncob.count('yellow')))
#print("Amount of purple kernels: " + str(corncob.count('purple')))
