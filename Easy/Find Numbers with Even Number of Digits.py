class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_nums = filter(lambda n: len(str(n)) % 2 == 0, nums)
        even_nums = list(even_nums)
        return len(even_nums)
      
      # You could also just use a for loop instead of filter
