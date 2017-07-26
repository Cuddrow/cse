list1 = [35, 45, 11, 9, 4.5, 6, 91, 18, 45, 54, 3.4, 95.1, 17.4, 19.9, 71.5]
list2 = [90, 11, 23, 60, 1, 2, 1, 17, 50, 13, 29]

list1 = sorted(list1)
list2 = sorted(list2)
list2.reverse()
#print (list1)
#print (list2)
#print(len(list1))
#print(len(list2))
print (len(list1))
print (len(list2))
del list1[0]
print (list1)
del list1[-3:]
print(len(list1))
print(len(list2))

print (sum(list1))
print (420-(sum(list1)))
print (sum(list2))
list2.append(-87)
print (sum(list2))
