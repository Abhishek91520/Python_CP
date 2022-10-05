def isPalindrome(string):
	return string == string[::-1]


s = input("Enter String :: ")
check = isPalindrome(s)

if check:
	print(f"Yes {s} is a palindrome string.")
else:
	print(f"No {s} is not a palindrome string.")
