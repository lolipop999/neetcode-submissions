class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int n : nums) {
            boolean added = set.add(n);
            if (!added) {
                return true;
            }
        }
        return false;
    }
}