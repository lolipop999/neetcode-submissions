class Solution:
    def getSum(self, a: int, b: int) -> int:
        # XOR (^)
        # &&
        # << shift left
        # >> shift right
        c = 0
        res = 0
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask
        for i in range(32):
            charA = a & 1
            charB = b & 1
            if (charA ^ charB) == 0:
                if charA == 0:
                    # position is 0
                    # carry is 0
                    if c == 1:
                        res = res | (1 << i)
                        c = 0
                else:
                    if c == 1:
                        res = res | (1 << i)
                    c = 1
            else:
                if c == 1:
                    c = 1
                else:
                    res = res | (1 << i)
                    c = 0
            a = a >> 1
            b = b >> 1

        if res & (1 << 31):
            res -= 1 << 32
            
        return res
