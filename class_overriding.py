class Parent:        # define class parent
   def myMethod(self):
      print "Calling parent method"

class Child(Parent): # define class child
   def myMethod(self):
      print "Calling child method"

c = Child()          # instance of child
c.myMethod()         # child calls overridden method