import math
from pylab import *

mole = 6.022 * (10**23)

pH = [-1.74]

appender = -1
for i in range(16):
    pH.append(appender)
    appender = appender + 1

print (pH)
savetxt('phvalues.csv', pH, fmt='%.2f', delimiter=',')

conc = [55.55, 10, 1]
conc_appender = 1
for i in range(14):
    conc_appender = conc_appender/10
    conc.append(conc_appender)

print(conc)
savetxt('concentrations.csv', conc, delimiter=',', fmt='%10.15f')
