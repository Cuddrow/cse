import math
from pylab import *
import pandas as pd

pH = pd.read_csv('phvalues.csv', names=['pH'])
pH = list(pH['pH'])
print (type(pH[0]))

concentrations = pd.read_csv('concentrations.csv', names=['Concentrations'])
concentrations = list(concentrations['Concentrations'])
print (type(concentrations[0]))

print (pH)
print (concentrations)

plot(concentrations, pH)
#xscale('log')
show()
