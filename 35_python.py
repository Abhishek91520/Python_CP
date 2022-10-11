def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

num = int(intput("Enter Decimal Number :: "))
  
convertToBinary(num)
print()
