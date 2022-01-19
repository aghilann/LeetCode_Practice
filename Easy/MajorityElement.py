class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        
        for n in nums:
            if dict.get(str(n)) == None:
                dict[str(n)] = 1
            else:
              z = dict[str(n)]
              dict[str(n)] = z + 1
        
        majority_element_count = 0
        majority_element = 0
        
        for key in dict:
          if dict[key] >= majority_element_count:
            majority_element_count = dict[key]
            majority_element = int(key)
        
        return majority_element
        # The first question I solved using a Hashmap, I intend to start doing more Hash Map questions.
