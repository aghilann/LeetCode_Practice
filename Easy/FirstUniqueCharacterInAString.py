class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict = {}
        
        for char in s:
            if not (char in dict):
                dict[char] = 1
            else:
                dict[char] = dict[char] + 1
        
        #print(dict)
        
        for key in dict:
            if dict[key] == 1:
                return s.index(key)
        return -1
