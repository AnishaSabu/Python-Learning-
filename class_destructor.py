class point:
  def __init(self,x=0,y=0):
    self.x=x
    self.y=y
  def __del__(self): #destructor
     class_name=self.__class__.__name__
     print class_name,"destroyed"
pt1=point() #object reference count becomes 1
pt2=pt1     #object reference count becomes 2
pt3=pt1     #object reference count becomes 3
print id(pt1),id(pt2),id(pt3)
del pt1     #object reference count becomes 2
del pt2     #object reference count becomes 1
del pt3     #object reference count becomes 0