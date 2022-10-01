num = int(input("Enter a number: "))
sum = 0
t = num
while t > 0:
   d = t % 10
   sum += d ** 3
   t //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
