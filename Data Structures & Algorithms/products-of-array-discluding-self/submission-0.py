class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        for i in range(length):
            for j in range(i+1, i+length):
                output[i] *= nums[j]
            nums.append(nums[i])

        return output
