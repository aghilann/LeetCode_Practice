class Solution:
    def isHappy(self, n: int) -> bool:
        prior = {}
        while n != 1:
            n = str(n)
            n = list(n)
            n = map(lambda x: (int(x))**2, n)
            n = sum(n)
            if prior.get(str(n)):
                return False
            prior[str(n)] = 1
        
        return True
