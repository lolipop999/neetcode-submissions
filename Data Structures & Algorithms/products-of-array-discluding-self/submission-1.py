class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, output = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        postfix[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        output[0] = postfix[1]
        output[len(nums)-1] = prefix[len(nums)-2]
        for i in range(1, len(nums)-1):
            output[i] = prefix[i-1] * postfix[i+1]
        return output