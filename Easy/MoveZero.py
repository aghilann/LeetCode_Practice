class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        looper = nums.copy()
        
        for n in looper:
            if n == 0:
                nums.remove(n)
                nums.append(n)
