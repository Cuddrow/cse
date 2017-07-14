import datetime as dt
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import csv
import numpy as np
import math

timearray = []
temparray = []
lightarray = []

timeformat = '%Y-%m-%d %H:%M:%S.%f'


def aligner(a_temparray, a_timearray):
    temp_length = len(temparray)
    time_length = len(timearray)
    diff = temp_length - time_length
    difference = (diff**2)
    difference = math.sqrt(difference)
    difference = int(difference)
    
    while difference != 0:
        difference = int(difference)
        print difference
        
        if temp_length > time_length:
            print 'temp loop entered'
            del a_temparray[(temp_length - (difference)):temp_length]
            temp_length = len(a_temparray)
            difference = temp_length - time_length
            difference = (difference**2)
            difference = math.sqrt(difference)
            difference = int(difference)
            #print temp_length
            
        elif time_length > temp_length:
            print 'time loop entered'
            del a_temparray[(time_length - (difference)):time_length]
            time_length = len(a_timearray)
            difference = temp_length - time_length
            difference = (difference**2)
            difference = math.sqrt(difference)
            difference = int(difference)
            #print time_length
            #print temp_length
            

    return a_temparray, a_timearray


    
    
myear = raw_input('Input year to plot in format XXXX: ')
mmonth = raw_input('Input month to plot in format XX: ')
mday = raw_input('Input day to plot in format XX: ')
file_time = myear + ' ' + mmonth + ' ' + mday

timereader = csv.reader(open('timearray' + file_time + '.csv', 'r'), delimiter=' ')
for row in timereader:
    r = float(row[0])
    t = dt.datetime.fromtimestamp(r)
    timearray.append(t)



tempreader = csv.reader(open('temparray' + file_time + '.csv', 'r'), delimiter=' ')
for row in tempreader:
    temp = float(row[0])
    print temp
    temparray.append(temp)
    
Ftemparray, Ftimearray = aligner(temparray, timearray)


#print temparray
#print timearray

fig, ax = plt.subplots()

ax.plot_date(Ftimearray, Ftemparray, '-')
ax.set_ylim([0,30])
plt.xticks(range(10))
    
ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

plt.show()
