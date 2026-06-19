class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = int((l + r) / 2)
            if (nums[m] == target):
                return m
            elif (nums[l] == target):
                return l
            elif (nums[r] == target):
                return r
            
            if (nums[m] > nums[l]): # the left side is sorted
                if (target < nums[m] and target > nums[l]): # on the left side 
                    r = m - 1
                else: # could be on the right side
                    l = m + 1
            else: # right side is sorted
                if target > nums[m] and target < nums[r]: # number is on the right side
                    l = m + 1
                else:
                    r = m - 1
        return -1