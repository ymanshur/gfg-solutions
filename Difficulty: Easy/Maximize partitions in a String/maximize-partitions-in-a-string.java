class Solution {
    public int maxPartitions(String s) {
        int partitions = 0;
        
        boolean[] visited = new boolean[26];
        boolean isPartition;
        
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            visited[s.charAt(i) - 'a'] = true;
            isPartition = true;
            
            for (int j = i + 1; j < n; j++) {
                if (visited[s.charAt(j) - 'a']) {
                    isPartition = false;
                    break;
                }
            }
            
            if (isPartition) {
                partitions++;
            }
        }
        
        // System.out.println(Arrays.toString(visited));
        
        return partitions;
    }
}