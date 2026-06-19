class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        min_value = nums[start]
        
        while True:
            mid = int((end + start) / 2)
            print("mid:" + str(mid))
            if nums[mid] > nums[end]:
                print(nums[mid], nums[end])
                start = mid + 1
                min_value = min(min_value, nums[end])
            elif nums[mid] < nums[start]:
                end = mid - 1
                print("yes")
                min_value = min(min_value, nums[mid])
            else:
                print(nums[mid], nums[start], nums[end])
                min_value = min(min_value, nums[start], nums[end])
                break
        return min_value