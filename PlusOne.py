class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        z = map(lambda x: str(x), digits)
        x = "".join(z)
        num = int(x)
        num += 1
        arr = list(str(num))
        return arr
        
