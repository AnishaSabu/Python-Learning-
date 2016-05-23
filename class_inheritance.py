class parent: #parent class
  parentattr=100
  def init(self):
    print "calling parent constructor"
  def parentmethod(self):
    print "calling parent method"
  def setattr(self,attr):
    parent.parentattr=attr
  def getattr(self):
    print "parent attribute= ",parent.parentattr
class child(parent): #child class
 def init(self):
  print "calling child constructor"
 def childmethod(self):
  print "calling child method"
c=child()
c.childmethod
c.parentmethod
c.setattr(400)
c.getattr()
