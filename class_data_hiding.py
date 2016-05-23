class count:
 __secretcount=0 #hidding attribute from direct access
 def start(self):
  self.__secretcount += 1
  print self.__secretcount
a=count()
a.start()
a.start()
#a.start()
print a.__secretcount #since the attribute is hidden