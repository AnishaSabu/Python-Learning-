num=int(raw_input("enter the number of groups: ")) #enter number of groups present
students_data={}      #declare an empty dictionary 
for i in range(1,num+1): 
  limit=int(raw_input("enter the number of student in %d group: "%i)) #enter the number of students in ith group
  students_data[i]={}       #to make each item of student_data dictionary, another dictionary
  for j in range(limit): #to enter the names of students in ith group
    students_data[i][j]=raw_input("enter the name of the student: ")
groupnum=int(raw_input("enter the roll no of the student: ")) #to enter each name
if groupnum in students_data.keys(): #to enter group number whose member's list is required
  print "students names in the entered group number" 
  print students_data[groupnum]    #to print list of students in the desired group