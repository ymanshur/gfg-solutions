class Solution {
    public ArrayList<Integer> kLargest(int[] arr, int k) {
        //Arrays.sort(arr);
        
        int n = arr.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>(n);
        
        for (int x : arr) {
            pq.add(-x);
        }

        ArrayList<Integer> res = new ArrayList<>(k);
        for (int i = 0; i < k; i++) {
            if (!pq.isEmpty()) {
                int x = pq.poll();
                res.add(-x);
            }
        }
        
        return res;
    }
}
