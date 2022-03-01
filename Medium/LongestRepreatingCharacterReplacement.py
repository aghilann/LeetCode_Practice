class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        chars = {}
        res = 0
        while r < len(s):
            chars[s[r]] = chars.get(s[r], 0) + 1
            majElem = max(chars, key=chars.get)
            
            if r-l+1-chars[majElem] > k:
                chars[s[l]] = chars[s[l]] - 1
                l += 1
            res = max(res, r-l+1)
            r += 1
            
        return res
                
            
          
