class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "nothing"
        encoded_str = ""
        for string in strs:
            encoded_str += " *" + string
        encoded_str = encoded_str[2:]
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "nothing":
            return []
        strings = s.split(" *")
        return strings
