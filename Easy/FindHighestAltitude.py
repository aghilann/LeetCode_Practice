class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        c_al = 0
        
        for g in gain:
            c_al += g
            
            if c_al > highest:
                highest = c_al
                
        return highest
