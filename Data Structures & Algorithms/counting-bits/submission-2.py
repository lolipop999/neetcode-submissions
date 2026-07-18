class Solution:
    def countBits(self, n: int) -> List[int]:
        # dynamic programming solution
        res = [0]
        hashmap = {}
        # if factor of 2, add to hashmap
        lastMult = 0
        for i in range(1, n+1):
            if i == 1:
                res.append(1)
                hashmap[i] = 1
            elif (i & (i - 1)) == 0:
                hashmap[i] = 1
                lastMult = i
                res.append(1)
            else:
                ones = hashmap[i - lastMult]+1
                res.append(ones)
                hashmap[i] = ones
        return res
            
            