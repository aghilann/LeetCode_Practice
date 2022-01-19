class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index = 0
        
        def get_product(n):
            x = nums.copy()
            x.remove(n)
            
            product_rest = 1
            
            for p in x:
                product_rest *= p
            
            return product_rest
        
        answer = list(map(get_product, nums))
        
        return answer
        
        # This solution runs in O(n^2) as uses a brute force approach - failed question.
            
