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

class Solution {
    // Function to find the height of a binary tree.
    int height(Node node) {
        if (node == null) {
            return -1;
        }
        
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);
        int maxHeight = Math.max(leftHeight, rightHeight);
        
        //System.out.printf("%d data=%d\n", maxHeight + 1, node.data);
        
        return maxHeight + 1;
    }
}