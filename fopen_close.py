fo = open("file.txt", "w") #opened a file
print "Name of the file: ", fo.name #to print name of file
print "Closed or not : ", fo.closed #to know whether file is closed or not
print "Opening mode : ", fo.mode    #to know in which mode the file is opened
print "Softspace flag : ", fo.softspace #to know whether space explicitly required with print
fo.close()             #closing file
print "Closed or not : ", fo.closed 