class Solution:
    def isValid(self, s: str) -> bool:
        openQ = []
        closeQ = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                openQ.append(s[i])
            else: # close bracket, check if there is corresponding open
                if openQ:
                    if abs(ord(s[i]) - ord(openQ.pop())) > 2:
                        return False
                else:
                    return False
        if openQ:
            return False
        return True
        