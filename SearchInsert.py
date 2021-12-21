class Solution:
    def searchInsert(self, nums, target):
        flag = 0
        for i, n in enumerate(nums):
            if target < n:
                flag = i
                break
            elif n == target:
                flag = i
                break
            elif i == len(nums) - 1:  # At last index
                flag = i + 1
                break
            elif (n < target) and (target < nums[i+1]):
                flag = i + 1
                break
        return flag
