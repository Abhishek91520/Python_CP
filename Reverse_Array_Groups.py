# Reverse an Array in groups
def reverse(arr, n, k):
	i = 0
	while(i<n):
		left = i
		right = min(i + k - 1, n - 1)
		while (left < right):
			arr[left], arr[right] = arr[right], arr[left]
			left+= 1;
			right-=1
		i+= k
	
# Driver code
arr = [1, 2, 3, 4, 5, 6,
				7, 8]

k = 3
n = len(arr)
reverse(arr, n, k)

for i in range(0, n):
		print(arr[i], end =" ")
