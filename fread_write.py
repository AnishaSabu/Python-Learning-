f=open("file.txt","wb") #open a file in write mode
f.write("I have opened a file.\n It is in write mode.")#write a string to file
f.close() #close file
 
f=open("file.txt","r+") #open file in read mode
str=f.read(43) #read string upto 43 bytes
print "the string is : ",str  

position=f.tell() #to know the present position
print "present position is: ",position

position=f.seek(0,0) #to change  present position to the beginning of file
str=f.read(43) #again read string upto 43 bytes
print "again string is: ",str
f.close()
