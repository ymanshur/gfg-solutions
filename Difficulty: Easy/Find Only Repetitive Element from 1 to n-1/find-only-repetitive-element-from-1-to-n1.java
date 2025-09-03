// User function Template for Java
class Solution {
    public int findDuplicate(int[] arr) {
        // Arrays.sort(arr);
        
        // for (int i = 0; i < arr.length; i++) {
        //     if (arr[i] == arr[i + 1]) {
        //         return arr[i];
        //     }
        // }
        
        // int n = arr.length;
        // int[] hash = new int[n - 1];
        
        // for (int i = 0; i < n; i++) {
        //     if (hash[arr[i] - 1] > 0) {
        //         return arr[i];
        //     }
            
        //     hash[arr[i] - 1]++;
        // }
        
        // return -1;
        
        int res = 0;
        for (int i = 0; i < arr.length; i++) {
            res ^= arr[i];
        }
        
        for (int i = 1; i < arr.length; i++) {
            res ^= i;
        }
        
        return res;
    }
}