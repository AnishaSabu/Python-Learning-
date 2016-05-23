class employee:   #defining class named as employee
  empcount=0      #class variable
  def __init__(self,name,salary):  #class constructor
    self.name=name
    self.salary=salary
    employee.empcount += 1 #count
    print "hello" 
  def displaycount(self):  
    print "no of employee: "%employee.empcount
  def displayemployee(self):
    print "name: ",self.name, "salary: ",self.salary

emp1=employee("aditya",2000)  #to create first object of class employee
emp2=employee("akanksha",3000)#to creste second object of class employee
emp3=employee("ankit",1000)   #to create third object of class employee
emp1.displayemployee()
emp2.displayemployee()

print "total no of employee: ",employee.empcount
print employee.__name__#prints name of class
print employee.__module__#prints the module in which class is defined
