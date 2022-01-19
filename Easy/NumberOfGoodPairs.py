class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        gp = 0
        
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b and i1 != i2:
                    gp += 1
                    
        return int(gp / 2)
      
 # This is a pretty bad solution since it has O(n^2) time complexity/
