class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort strategy
        hashmap = defaultdict(int)
        size = len(nums)
        for i in range(size):
            hashmap[nums[i]] += 1
        repeats = [[] for _ in range(size+1)]
        for key, value in hashmap.items():
            repeats[value].append(key)
        ans = []
        i = size
        while (len(ans) < k):
            for j in range(len(repeats[i])):
                ans.append(repeats[i][j])
            i -= 1
        return ans
        