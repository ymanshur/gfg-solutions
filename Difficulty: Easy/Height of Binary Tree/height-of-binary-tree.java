/*
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
}
 */
 
import java.util.*;

class Solution {
    // Function to find the height of a binary tree.
    int height(Node node) {
        if (node == null) {
            return 0;
        }
        
        Queue<Node> queue = new LinkedList<>();
        
        queue.add(node);
        int level = 0;
        int n; // current queue size
        
        while (!queue.isEmpty()) {
            // for (Node elem : queue) {
            //     System.out.printf("%d ", elem.data);
            // }
            // System.out.println();
            
            n = queue.size();
            
            for (int i = 0; i < n; i++) {
                Node curr = queue.poll();
                
                if (curr.left != null) {
                    queue.add(curr.left);
                }
                
                if (curr.right != null) {
                    queue.add(curr.right);
                }
            }
            
            level++;
        }
        
        return level - 1;
    }
}