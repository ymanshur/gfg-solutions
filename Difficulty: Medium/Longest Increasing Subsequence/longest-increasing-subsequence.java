class Solution {
    static int lis(int arr[]) {
        int n = arr.length;
        
        int[] prefix = new int[n];
        prefix[0] = 1;
        
        int max = prefix[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = 1;
            
            int maxPrev = 0;
            for (int j = i - 1; j >= 0; j--) {
                if (arr[j] < arr[i]) {
                    if (prefix[j] > maxPrev) {
                        maxPrev = prefix[j];
                    }
                }
            }
            
            prefix[i] += maxPrev;
            
            if (prefix[i] > max) {
                max = prefix[i];
            }
        }
        
        // System.out.println(Arrays.toString((prefix)));
        
        return max;
    }
}