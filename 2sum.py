class Solution:
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            sta = nums[i]
            for j in range(i+1, len(nums)):
                if sta+nums[j] == target:

                    return [i,j]
                
sol = Solution()
print(sol.twoSum([2,7,4,15],11))