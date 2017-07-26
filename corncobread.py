import random
import numpy as np

corncob = np.loadtxt('cornkernels1.csv', dtype=(str), delimiter=',')
print ("Contents of loadedlist: " + str(corncob))

corncob = np.array(corncob).tolist()

a = corncob.count("yellow")
print("Amount of yellow kernels: " + str(corncob.count('yellow')))
print("Amount of yellow kernels: " + str(corncob.count('purple')))
