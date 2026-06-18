class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used_vals = set()
        ans = []
        for i in range(len(nums)-2):
            if (nums[i] in used_vals):
                continue
            used_vals.add(nums[i])
            
            # find the target using two pointers
            left = i+1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return ans
                

