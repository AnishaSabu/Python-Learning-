list=[1,2,4,3,5]
print("elements in the list")
for data in list:
 print data
print "elements in ascending order"
list.sort()
print list
print "elements in reverse order"
list.reverse()
print list
list.reverse()
print "number of times 3 is present in list: "
a=list.count(3)
print a
print "number of elements in list: "
b=len(list)
print b
print "appending a number 6 in list"
list.append(6)
print list
print "inserting a number 100 at 3rd position of list"
list.insert(3,100)
print list
print "removing the inserted number"
list.remove(100)
print list
c=max(list)
d=min(list)
print "maximum value in list"
print c
print "minimum value in list"
print d
print "whether 6 is present in list?"
if(6 in list):
  print "present"
else:
 print "absent"