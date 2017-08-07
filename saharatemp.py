from pylab import *
import pandas as pd
import random as rd

array_length = 96
templist = zeros(array_length)
timelist = arange(0,1440,15)

def plotter(templist, timelist):
    plot(timelist, templist, 'r-', label='Temperature')
    axis([0,1500,0,50])
    xlabel('Time in minutes')
    ylabel('Temperature')
    title(" Temperature for 24 hours in Sahara")
    legend(loc='upper left')
    show()

def tempgenerator():
    starting_temp = float(input("Input starting temperature"))
    templist[0] = starting_temp
    templist[1] = templist[0]+0.68
    mod_8_16 = 0.2
    mod_2030_2230 = 0.5
    for i in range(2,96,1):
        # From 08:00 to 16:00 - 32 steps - try increase of 0.68 per 15 minutes
        if i <= 32:
            templist[i] = (templist[i-1]+0.75)-((i/32)*mod_8_16)
        # From 16:00 to 18:00 - 8 steps
        elif i > 32 and i <= 40:
            templist[i] = templist[i-1] + rd.uniform(-0.2,0.2)
        # From 18 to 20:30 - 10 steps
        elif i > 40 and i <= 50:
            templist[i] = (templist[i-1] - 0.4)
        # From 20:30 to 22:30 - 10 steps - try reduction of 0.875 per 15 minutes
        elif i > 50 and i <= 60:
            templist[i] = templist[i-1] - (0.875+(rd.uniform(-0.2,0.2)))
        # From 22:30 to 08:00 - 38 steps
        elif i > 60:
            templist[i] = templist[i-1] - (0.26+(rd.uniform(-0.05,0.05)))

#for index, temp in enumerate(templist):
#    print(index,round(temp,3))



plotter(templist,timelist)
save_array = [templist, timelist]

saveframe = pd.DataFrame({"Temperature" : templist, "Time" : timelist})
#print(saveframe)
saveframe.to_csv("saharadata2.csv", index=False)
