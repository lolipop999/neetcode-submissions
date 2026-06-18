class Solution:
    def isValid(self, s: str) -> bool:
        openQ = []
        match = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] in match:
                if openQ and openQ[-1] == match[s[i]]:
                    openQ.pop()
                else:
                    return False
            else:
                openQ.append(s[i]) 
        return False if openQ else True
        