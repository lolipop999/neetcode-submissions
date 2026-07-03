class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        while n-1 > 0:
            n -= 1
            temp = one
            one = one + two
            two = temp
        return one
