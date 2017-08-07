from pylab import *
import numpy as np

potatoes = np.loadtxt('potatoweightsnoheaders.csv', delimiter=',', unpack=True)
print(potatoes)
print(potatoes[2][3])
starting_weights = potatoes[0]
final_weights = potatoes[1]
concentrations = potatoes[2]

#This method solves decimal errors when converting an array to a list.
x = np.array(potatoes[2]).tolist()
print(x)
print(type(x))

z = list(concentrations)
print(z)
print(str(z[3]))


#print (starting_weights)
#print (final_weights)
#print (concentrations)
