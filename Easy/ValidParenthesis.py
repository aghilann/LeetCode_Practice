class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposite = {"(": ")", "[": "]", "{": "}"}
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            elif bracket == ")" or bracket == "]" or bracket == "}":
                
                if len(stack) == 0:
                    return False
                opener = stack.pop()
                
                if opposite[opener] != bracket:
                    return False
        
        return len(stack) == 0
            
