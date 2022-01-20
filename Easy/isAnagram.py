class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
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
        
        return dict1 == dict2
        
