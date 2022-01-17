'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''
# This question had a lot of edge cases such as the length being less then 3, or the Mountain starts/ends from the max (a case I didn't initially consider)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        mx = max(arr)
        mx_index = arr.index(mx)
        
        if mx == arr[-1] or mx == arr[0]:
            return False
        
        left = arr[:mx_index + 1] # Includes max
        prev1 = arr[0] - 1
        
        for n in left:
            if n <= prev1:
                return False
            prev1 = n
          
        
        right = arr[mx_index:]
        prev2 = mx + 1
        
        for n in right:
            if n >= prev2:
                return False
            prev2 = n
            
        return True
