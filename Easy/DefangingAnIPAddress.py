class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join(list(map(lambda c: "[.]" if c == "." else c, address)))
