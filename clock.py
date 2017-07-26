import pylab
import matplotlib.pyplot as plt
import numpy as np

time_of_day = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"
, "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"]
sun_angle = [0, 0, 0, 0, 0, 3, 9, 17, 24, 31, 38, 45, 48, 52, 51, 47, 43, 36, 28, 22, 14, 7, 1, 0, 0]

print (len(time_of_day))
print (len(sun_angle))

plt.plot()
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
pylab.show()
