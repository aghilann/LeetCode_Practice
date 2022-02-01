class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        
        
        def recurse(y, x):
        
            if y > (m - 1) or x > (n - 1):
                #memo[(y, x)] = 0
                return 0
                

            elif x == (n - 1) and y == (m - 1):
                #memo[(y, x)] = 1
                return 1

            else:
                
                first = 0
                second = 0

                if memo.get((y+1, x)):
                    first = memo.get((y+1, x))
                else:
                    first = recurse(y+1, x)
                    memo[(y+1, x)] = first

                if memo.get((y, x+1)):
                    second = memo.get((y, x+1))
                else:
                    second = recurse(y, x+1)
                    memo[(y, x+1)] = second
                    
                return first + second
            # I watched a Hackerank video on Dynamic Programming
            # This question was explained in Psedocode so this solution is not entirely mine.

        return recurse(0, 0)
