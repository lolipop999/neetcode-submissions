class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hashmap = {}
        
        if amount == 0:
            return 0

        for i in range(1, amount+1):
            best = amount + 1
            for c in coins:
                if i - c == 0:
                    print(i, c)
                    hashmap[i] = 1
                    break
                elif i - c in hashmap:
                    best = min(best, 1 + hashmap[i-c])
                    hashmap[i] = best

        if amount in hashmap:
            return hashmap[amount]
        else:
            return -1