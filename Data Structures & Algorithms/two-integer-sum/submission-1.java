class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seenVals = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int val = target - nums[i];
            if (seenVals.containsKey(val)) {
                return new int[]{seenVals.get(val), i};
            }
            seenVals.put(nums[i], i);
        }
        return new int[]{};
    }
}
