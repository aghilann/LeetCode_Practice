'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        visited = []
        
        for z in arr:
            if z / 2 in visited or z * 2 in visited:
                return True
            visited.append(z)
        return False
        
