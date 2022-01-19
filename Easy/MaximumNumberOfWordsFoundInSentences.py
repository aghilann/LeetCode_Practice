class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        def word_count(str):
            return len(str.split())
        
        return max(list(map(word_count, sentences)))
        
