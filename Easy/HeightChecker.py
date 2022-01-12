class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ct = 0
        ct2 = 0
        expected = sorted(heights)
        for i, h in enumerate(heights):
            if h == expected[i]:
                ct += 1
            ct2 += 1
        
        return ct2 - ct
