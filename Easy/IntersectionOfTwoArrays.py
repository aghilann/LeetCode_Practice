class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Let m = len(num1)
        # Let n = len(num2)
        
        dict = {} # O(n) Space Complexity
        intersection = [] # O(n)
        
        for n in set(nums2): # O(n) Time Complexity
            dict[str(n)] = 1
        
        for n in set(nums1): # O(m) Time Complexity
            if dict.get(str(n)):
                intersection.append(n)
        
        return intersection 
        
        
                
        
