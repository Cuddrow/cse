height = [176, 169, 172, 172, 179, 160, 157, 170, 190, 154, 181, 185, 168, 184]
age = [34, 33, 27, 31, 19, 34, 22, 28, 23, 32, 20, 20, 24, 30, 21, 25]
weight = [62, 46, 56, 52, 80, 51, 84, 65, 92, 55, 53, 52, 84, 84, 61]

del age[14:16]
del weight[14]

heightsum = sum(height)
agesum = sum(age)
weightsum = sum(weight)

print(len(height))
print(len(age))
print(len(weight))

avgheight = int(heightsum/len(height))
avgage = int(agesum/len(age))
avgweight = int(weightsum/len(weight))

print ("Average height is: " + str(avgheight))
print ("Average age is: " + str(avgage))
print ("Average weight is: " + str(avgweight))

countheight = height.count(avgheight)
countage = age.count(avgage)
countweight = weight.count(avgweight)

print("Amount of students at average height of %s is %s" % (avgheight, countheight))
print("Amount of students at average age of %s is %s" % (avgage, countage))
print("Amount of students at average weight of %s is %s" % (avgweight, countweight))
