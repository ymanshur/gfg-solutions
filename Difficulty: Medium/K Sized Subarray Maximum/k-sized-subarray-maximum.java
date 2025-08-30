class Solution {
    static class Pair {
        int first;
        int second;
        
        Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
    
    public ArrayList<Integer> maxOfSubarrays(int[] arr, int k) {
        ArrayList<Integer> res = new ArrayList<>();
        
        PriorityQueue<Pair> heap = new PriorityQueue<>(new Comparator<>() {
            public int compare(Pair a, Pair b) {
                return b.first - a.first; // descending order
            }
        });
        
        for (int i = 0; i < k; i++) {
            heap.add(new Pair(arr[i], i));
        }
        
        res.add(heap.peek().first);
        
        //          0  1  2  3  4  5  6  7  8 
        // arr[] = [1, 2, 3, 1 ,4, 5, 2, 3, 6], k = 3
        //                               i
        
        int n = arr.length;
        int max;
        for (int i = k; i < n; i++ ) {
            heap.add(new Pair(arr[i], i));
            
            
            while (heap.peek().second < i - k + 1) {
                heap.poll();
            }
            
            max = heap.peek().first;
            res.add(max);
        }
        
        
        return res;
    }
}