class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#         max_1 = max(nums)
#         arr1 = list(filter(lambda n: max_1 != n, nums))
        
#         if arr1 == []:
#             return max_1
        
#         max_2 = max(arr1)
#         arr2 = list(filter(lambda n: max_2 != n, arr1))
        
#         if arr2 == []:
#             return max_1
        
#         return max(arr2)

        
        nums = list(set(nums))
        max1 = max(nums)
    
        nums.remove(max1)
        
        if nums == []:
            return max1
    
        max2 = max(nums)
        nums.remove(max2)
        
        if nums == []:
            return max1
        
        return max(nums)
