from pylab import *
import datetime as dt

timelist = loadtxt('./temp_file_store/timearray31jan.csv', delimiter=',')
print ("length of list " + str(len(timelist)))

#Syntax for directly printing timestamp as a time of day
#print ((dt.datetime.fromtimestamp(timelist[0])).strftime('%H:%M:%S'))
#print ((dt.datetime.fromtimestamp(timelist[1])).strftime('%H:%M:%S'))
#print ((dt.datetime.fromtimestamp(timelist[2])).strftime('%H:%M:%S'))
#print ((dt.datetime.fromtimestamp(timelist[3])).strftime('%H:%M:%S'))
