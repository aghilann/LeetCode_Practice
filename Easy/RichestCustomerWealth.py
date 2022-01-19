class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        return max(map(sum, accounts))
        
        
'''
Success
Details 
Runtime: 40 ms, faster than 99.78% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.3 MB, less than 59.40% of Python3 online submissions for Richest Customer Wealth.
'''
