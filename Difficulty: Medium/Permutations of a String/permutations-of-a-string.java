class Solution {
    private static int n;
    
    private void permute(ArrayList<String> res,
                         Map<Character, Integer> counter,
                         StringBuilder curr) {
        if (curr.length() == n) {
            res.add(curr.toString());
            return;
        }
        
        for (Map.Entry<Character, Integer> entry : counter.entrySet()) {
            char c = entry.getKey();
            int count = entry.getValue();
            
            if (count == 0) {
                continue;
            }
            
            curr.append(c);
            counter.put(c, count - 1);
            
            permute(res, counter, curr);
            
            // Backtrack: remove the character and restore its count
            
            curr.deleteCharAt(curr.length() - 1);
            counter.put(c, count);
        }
    }
    
    public ArrayList<String> findPermutation(String s) {
        n = s.length();
        
        ArrayList<String> res = new ArrayList<>();
        
        // Frequency map to count occurrances of each character
        Map<Character, Integer> counter = new HashMap<>();
        
        // Populate the frequency map with the characters of the input string
        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }
        
        // Initialize a permutation builder;
        StringBuilder curr = new StringBuilder();
        
        permute(res, counter, curr);
        
        
        return res;
    }
}