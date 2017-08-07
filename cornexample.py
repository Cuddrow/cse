import pandas as pd

corncob = pd.read_csv('cornkernels1.csv', names=['color'])
corncob = (list(corncob['color']))
