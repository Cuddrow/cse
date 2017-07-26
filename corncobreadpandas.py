import random
import numpy as np
import pandas

corncobimport = pandas.read_csv('cornkernels1.csv')
print ("Contents of loadedlist: " + str(corncobimport))
corncob = list(corncobimport)

print(type(corncob))
print(len(corncob))
print(corncob)
print("Amount of yellow kernels: " + str(corncob.count('yellow')))
print("Amount of purple kernels: " + str(corncob.count('purple')))
