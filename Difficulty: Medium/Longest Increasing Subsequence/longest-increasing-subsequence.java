class Solution {
    static int lis(int arr[]) {
        int n = arr.length;
        
        int[] prefix = new int[n];
        
        for (int i = 0; i < n; i++) {
            prefix[i] = 1;
            
            for (int j = i - 1; j >= 0; j--) {
                if (arr[j] < arr[i] && prefix[j] + 1 > prefix[i]) {
                    prefix[i] = prefix[j] + 1;
                }
            }
        }
        
        int max = 1;
        for (int i = 0; i < n; i++) {
            if (prefix[i] > max) {
                max = prefix[i];
            }
        }
        
        // System.out.println(Arrays.toString((prefix)));
        
        return max;
    }
}