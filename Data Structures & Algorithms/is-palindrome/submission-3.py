class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

        front = 0
        back = len(s) - 1
        s = s.lower()
        while front < back:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[back].isalnum():
                back -= 1
                continue
            if s[front] == s[back]:
                front += 1
                back -= 1
            else:
                return False
        return True
        