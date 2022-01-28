class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        index = 0
        answer = [0] * len(queries)
        
        for i, cpoint in enumerate(queries):
            for ppoint in points:
            
                cord = ppoint
                circ = cpoint
                radius = circ[2]

                dx = cord[0] - circ[0]
                dy = cord[1] - circ[1]

                distance = (dx**2 + dy**2)**0.5

                if distance <= radius:
                    answer[i] = answer[i] + 1
            
        return answer
