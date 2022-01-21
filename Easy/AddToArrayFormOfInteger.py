class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        z = map(lambda x: str(x), num)
        x = "".join(z)
        n = int(x)
        n += k
        arr = list(str(n))
        return arr
