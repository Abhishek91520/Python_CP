def recurSum(n):
	if n <= 1:
		return n
	return n + recurSum(n - 1)

number = int(input("Enter a number : "))
print(recurSum(number))
