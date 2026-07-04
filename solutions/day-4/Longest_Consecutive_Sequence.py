class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        HashSet<Integer> set = new HashSet<>();
        for (int val : nums) set.add(val);

        int maxLen = 0;

        for (int val : set) {
            // only start counting from the beginning of a sequence
            if (!set.contains(val - 1)) {
                long length = 1;
                long next = (long) val + 1;
                while (set.contains((int) next) && next <= Integer.MAX_VALUE) {
                    length++;
                    next++;
                }
                maxLen = (int) Math.max(maxLen, length);
            }
        }

        return maxLen;
    }
}
