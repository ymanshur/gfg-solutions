class TrieNode {
    TrieNode[] children;
    boolean isEndOfWord;
    
    TrieNode() {
        children = new TrieNode[26];
        isEndOfWord = false;
    }
}

// User function Template for Java
class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Insert a word into the Trie
    public void insert(String word) {
        TrieNode curr = root;
        
        int n = word.length();
        int childAt;
        for (int i = 0; i < n; i++) {
            childAt = word.charAt(i) - 'a';
            
            if (curr.children[childAt] == null) {
                curr.children[childAt] = new TrieNode();
            }
            
            curr = curr.children[childAt];
        }
        
        curr.isEndOfWord = true;
    }

    // Search for a word in the Trie
    public boolean search(String word) {
        TrieNode curr = root;
        
        int n = word.length();
        int childAt;
        for (int i = 0; i < n; i++) {
            childAt = word.charAt(i) - 'a';
            
            if (curr.children[childAt] == null) {
                return false;
            }
            
            curr = curr.children[childAt];
        }
        
        return curr.isEndOfWord;
    }

    // Check if a prefix exists in the Trie
    public boolean isPrefix(String word) {
        TrieNode curr = root;
        
        int n = word.length();
        int childAt;
        for (int i = 0; i < n; i++) {
            childAt = word.charAt(i) - 'a';
            
            if (curr.children[childAt] == null) {
                return false;
            }
            
            curr = curr.children[childAt];
        }
        
        return true;
    }
}

