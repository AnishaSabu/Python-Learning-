list=[]
i=int(raw_input("enter the number of elements in list: "))
print "enter the elements: "
for j in range(i):
   list.append(input())
print list
large=list[0]
for j in range(i):
   if list[j]>large:
      large=list[j]
print "largest element in list: %d"%(large)