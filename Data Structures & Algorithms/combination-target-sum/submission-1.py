class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursive problem
        # start w/ lowest, subtract from target, find new combinationSum
        # if it doesn't work, remove the last value added
        nums.sort()
        res = []
        nums_used = []
        def findSum(target, val, i):
            target -= val
            if target < 0:
                return
            nums_used.append(val)
            if target == 0:
                res.append(nums_used.copy())
                nums_used.pop()
                return

            i = nums.index(val)
            for x in range(i, len(nums)):
                if target - nums[x] < 0:
                    break
                findSum(target, nums[x], i)
            nums_used.pop()    
            return
            
            
        for i in range(len(nums)):
            findSum(target, nums[i], i)

        return res