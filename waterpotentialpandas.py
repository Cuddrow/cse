import pandas as pd
from pylab import *

potatodata = pd.read_csv('potatodata.csv')
print(type(potatodata))
print(potatodata)
start = potatodata['start'].values
end = potatodata['end'].values
concentrations = potatodata['concentration'].values

diff = end-start

plot(concentrations, diff)
xlabel('Concentration in molar')
ylabel('Weight difference')
axis([-0.2,1,-2.5,2.5])
grid(True, which='both')

axhline(y=0, color='k')
axvline(x=0, color='k')
show()
