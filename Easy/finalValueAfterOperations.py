class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        
        for o in operations:
            if o == "--X" or o == "X--":
                X -= 1
            else:
                X+=1
        return X
