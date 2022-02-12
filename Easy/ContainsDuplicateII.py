class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict = {}
        
        for i, n in enumerate(nums):
            if dict.get((n), -1) + 1 and abs(dict[(n)] - i) <= k:
                return True
            else:
                dict[(n)] = i
        
        return False
                
        
