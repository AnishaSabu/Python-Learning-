list=[]
i=int(raw_input("enter the number of elements in list: "))
print "enter the elements: "
for j in range(i):
   list.append(input())
print list
if list[0]>list[1]:
   large=list[0]
else:
   large=list[1]
for j in range(i):
   if list[j]>large:
      large=list[j]
print "largest element in list: %d"%(large)