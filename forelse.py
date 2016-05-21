for num in range(50,100): #to take numbers  between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine whether it is a factor
         break            #to goto first for loop 
   else:                  
      print '%d is a prime number'%(num) #to print msg for prime numbers