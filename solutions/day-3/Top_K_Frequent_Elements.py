class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int val : nums) hm.put(val, hm.getOrDefault(val, 0) + 1);

        PriorityQueue<Integer> pr = new PriorityQueue<>((a, b) -> hm.get(b) - hm.get(a));
        for (int val : hm.keySet()) pr.add(val);

        int[] res = new int[k];
        for (int i = 0; i < res.length; i++) res[i] = pr.poll();

        return res;
    }
}
