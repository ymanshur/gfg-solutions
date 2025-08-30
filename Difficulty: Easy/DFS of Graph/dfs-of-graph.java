class Solution {
    static void traverse(
        ArrayList<ArrayList<Integer>> adj, 
        Map<Integer, Boolean> visited, 
        int v,
        ArrayList<Integer> res
    ) {
        res.add(v);
        visited.put(v, true);
        
        ArrayList<Integer> adjv = adj.get(v);
        
        int n = adjv.size();
        int v2;
        for (int i = 0; i < n; i++) {
            v2 = adjv.get(i);
            if (!visited.containsKey(v2)) {
                traverse(adj, visited, v2, res);
            }
        }
    }
    
    // Function to return a list containing the DFS traversal of the graph.
    public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
        ArrayList<Integer> res = new ArrayList<>();
        Map<Integer, Boolean> visited = new HashMap<>();
        
        traverse(adj, visited, 0, res);
        
        return res;
    }
}