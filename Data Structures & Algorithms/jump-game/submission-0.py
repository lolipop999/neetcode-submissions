class Solution:
    def canJump(self, nums: List[int]) -> bool:

        furthestAway = 1
        for i in range(len(nums)-2, -1, -1):
            print(i, nums[i], furthestAway)
            if nums[i] >= furthestAway:
                furthestAway = 1
            else:
                furthestAway += 1
        return True if furthestAway == 1 else False
