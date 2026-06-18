class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        sets = set()
        while left < right:
            if (abs(nums[left]) >= abs(nums[right])):
                temp = right
                while abs(nums[left]) <= 2*abs(nums[right]) and left < right: # once we get to half of the number
                    target = 0 - (nums[left] + nums[right])
                    if target in nums[left+1:right]:
                        print(str(target) + " is in")
                        sets.add((nums[left], target, nums[right]))
                    right -= 1
                right = temp
                left += 1
            if (abs(nums[left]) < abs(nums[right])):
                temp = left
                while abs(nums[right]) <= 2*abs(nums[left]) and left < right: # once we get to half of the number
                    target = 0 - (nums[left] + nums[right])
                    if target in nums[left+1:right]:
                        print(str(target) + " in")
                        sets.add((nums[left], target, nums[right]))
                    left += 1
                left = temp
                right -= 1
        res = [list(item) for item in sets]
        return res
            
                