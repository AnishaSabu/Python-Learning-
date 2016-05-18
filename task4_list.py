lowestrange=1500
highestrange=2700
list=[]
n=(highestrange-lowestrange)/5
for i in range(n):
   if (lowestrange+(5*i))%7==0:
      list.append(lowestrange+(5*i))
print "list of numbers divided by 7 and multiple of 5 between 1500 and 2700 : "
print list