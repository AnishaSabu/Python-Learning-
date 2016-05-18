list=[] #empty list
i=int(raw_input("enter the number of elements in list: "))
print "enter the elements: "
for j in range(i):
   list.append(input())#adding elements to the empty list
print list
i=0
sum=0
for data in list:
   sum=sum+list[i]
   i=i+1
print "sum:%d"%(sum)
 
