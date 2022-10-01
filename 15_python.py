l = int(input ("Enter the Lowest Range Value: "))  
u= int(input ("Enter the Upper Range Value: "))  
  
print ("Prime Numbers are: ")  
for n in range (l, u + 1):  
    if n > 1:  
        for i in range (2, n):  
            if (n % i) == 0:  
                break  
        else:  
            print (n) 
