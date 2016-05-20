number = int(raw_input("Enter the number of student : "))	#first we read the number of students
print "Number of Student : %d"%(number) 	#just print the number of student 
studentDB = {} #empty student dictionary (database)
subject = ["Sub1","Sub2","Sub3","Sub4","Sub5","Sub6"] #we can store subject name in a list 
for i in range(0,number):
	name = raw_input("Name:")
	studentDB[name] = {}#we create another dictionary for each student (inside studentDB)
	for i in subject:
		studentDB[name][i] = int(raw_input("Enter mark of %s"%(i)))
	'''
	##old way of reading each marks 
	studentDB[name]["Sub1"]=int(raw_input("Enter the mark of Sub1:")) #we read marks of 6 subject 
	studentDB[name]["Sub2"]=int(raw_input("Enter the mark of Sub2:"))
	studentDB[name]["Sub3"]=int(raw_input("Enter the mark of Sub3:"))
	studentDB[name]["Sub4"]=int(raw_input("Enter the mark of Sub4:"))
	studentDB[name]["Sub5"]=int(raw_input("Enter the mark of Sub5:"))
	studentDB[name]["Sub6"]=int(raw_input("Enter the mark of Sub6:"))
	'''

name = raw_input("Plz Enter the name of student:")	#THEN  we read a name of student whose avg marks is needed . 
if(name in studentDB.keys()): 
	avg = float(studentDB[name]["Sub1"]+studentDB[name]["Sub2"]+studentDB[name]["Sub3"]+studentDB[name]["Sub4"]+studentDB[name]["Sub5"]+studentDB[name]["Sub6"])/6
print "Average marks of %s : %f"%(name,avg)
