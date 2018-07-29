for num in range(10,20): #to iterate between 10 to 20
     for i in range(2,num): #to iterate on the factors of the number
        if num% i == 0:
         print '%d is num'%(num)
         print '%d is i'%(i)
         print"%d is not prime number" % (num)
         break
     else:
         print "%d is prime number"%(num)
