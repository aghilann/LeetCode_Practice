class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dict1 = {}
        
        for char in s:
            if not dict1.get(char):
                dict1[char] = 1
            else:
                dict1[char] = dict1[char] + 1
                
        dict2 = {}
        
        for char in t:
            if not dict2.get(char):
                dict2[char] = 1
            else:
                dict2[char] = dict2[char] + 1
        
        
        for char in dict2:
            if dict1.get(char) != dict2.get(char):
                return char
        
        
        
                
