class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "*" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        while len(s) > 0:
            temp = ""
            i = 0
            while True:
                if s[i] == "*":
                    s = s[1:]
                    break
                temp += s[i]
                s = s[1:]
            temp_int = int(temp)
            word = ""
            for i in range(temp_int):
                word += s[i]
            decoded_strs.append(word)
            s = s[temp_int:]
        return decoded_strs
