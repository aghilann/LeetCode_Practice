class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest = min(strs)
        #Shortest word
        
        prefix_sofar = ""
        
        ll = len(strs)
        
        def checkletter(i):
            return len(list(filter(lambda wd: wd[i] == shortest[i], strs))) == ll
        
        
        for i, s in enumerate(shortest):
            
            def checkletter(i):
                return len(list(filter(lambda wd: wd[i] == s, strs))) == ll
        
            if checkletter(i):
                prefix_sofar += s
        
            else:
                return prefix_sofar
        
        return prefix_sofar
            
            
