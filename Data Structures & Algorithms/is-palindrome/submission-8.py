class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        s = s.lower()
        while front < back:
            if not self.isAlnum(s[front]):
                front += 1
                continue
            if not self.isAlnum(s[back]):
                back -= 1
                continue
            if s[front] == s[back]:
                front += 1
                back -= 1
            else:
                return False
        return True
    
    def isAlnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9') or (ord('a') <= ord(c) <= ord('z')))