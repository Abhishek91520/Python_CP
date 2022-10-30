class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            midle = (left + right) // 2
            if target == nums[midle]:
                return midle
            elif target < nums[midle]:
                right = midle - 1
            else:
                left = midle + 1
        return -1

arr = list(map(int, input("Enter integers:- ").split()))
item = int(input("Enter Number to find:- "))
arr.sort()
index = Solution().search(arr, item)
print(f"Item found at {index}" if index != -1 else "Item not found")
