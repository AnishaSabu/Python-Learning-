import time;
T1=time.time()
print "current time: ",T1 #to print time in secs

Tlocal =  time.localtime(time.time())
print "local.time :",Tlocal #to print time in structure form

T=time.asctime(Tlocal)
print "asc.current time :",T #to print time in formatted form

import calendar
Calendar=calendar.month(2016,10)
print "the calender : ",Calendar #to print calendar 

print "time.altzone : ",time.altzone #to print altzone

def function(): #defining a function
  time.sleep(2.5) #to provide a lag of 2.5 secs
t=time.clock() 
function()
print "time.clock: ",time.clock()

t=time.clock()
function()
print "time.clock: ",time.clock()

print "time.ctime() : %s" %(time.ctime())


