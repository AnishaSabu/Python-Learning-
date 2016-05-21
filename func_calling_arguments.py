print "Function calling"
def printfunc(str): #defininf function to print string
   print str
   return
printfunc("Today i have to go to supermarket")  #calling function
printfunc("I have a long list to deal with")    #calling function

print "pass by reference"

def listfunc(list): #defining function
   list.append(89)  #list gets altered inside and outside function
   list=[1,2,3]     #list gets altered onliy inside the function
   print "list inside function: ",list
list=[4,5,6]
listfunc(list)      #calling function
print "list outside function: ",list

print "required arguments"
def listfunc(list):     #defining function 
   list.append([1,2,3]) #list gets altered inside and outside function
   print "list inside function: ",list
list=[4,5,6]
listfunc(list) #calling function
print "list outside function: ",list

print "keyboard arguments"
def data(name,age):     #defining function
    print "name: ",name
    print "age: ",age
data(age=3,name="anisha") #calling funtion with arguments changed order

print "default arguments" 
def data(name,age=1):     #defining function with one argument having a default value
    print "name: ",name
    print "age: ",age
data(name="anisha")       #while calling one argument is missing

print "variable length argument"
def func(arg,*vartuple): #defining function with variable lengthn arguments
    print "output is:",arg
    for var in vartuple:
       print var
    return
func(10)
func(1,2,3)

print "anonymous functions"
sum= lambda arg1,arg2:arg1+arg2 #defining anonymous functions
print " sumof 20 and 30 is : ",sum(20,30)
print " sumof 40 and 60 is : ",sum(40,60)



