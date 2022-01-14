class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        prior_arr = []
        
        for n in nums:
            if n == 1:
                prior_arr.append(n)
                if len(prior_arr) > max_so_far:
                    max_so_far = len(prior_arr)
            else:
                prior_arr = []
        
        return max_so_far
            
