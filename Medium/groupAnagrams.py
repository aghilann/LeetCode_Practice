class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}
        
        for s in strs:
            chars = list(s)
            chars = sorted(chars)
            sorted_string = "".join(chars)
            
            if dict.get(sorted_string):
                dict[sorted_string].append(s)
            
            else:
                dict[sorted_string] = [s]
             
        return dict.values()
            
