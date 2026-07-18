class Solution:
    def reverseBits(self, n: int) -> int:
        # reversing the bits
        res = 0
        for i in range(31, -1, -1):
            if n & 1 == 1: # if last number is 1
                res += 2 ** i
            n = n >> 1 # shift digits over
        return res
