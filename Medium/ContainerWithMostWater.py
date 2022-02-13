class Solution:
    def maxArea(self, height: List[int]) -> int:
        
#         max_area = 0
        
#         def area(x, y):
#             return min(height[x], height[y]) *  (y - x)
        
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):                
#                 ans = area(i, j)                                
#                 if ans > max_area:
#                     max_area *= 0
#                     max_area += ans
                    
#         return max_area
        
        l = 0
        r = len(height) - 1
        rsf = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            rsf = max(area, rsf)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return rsf
