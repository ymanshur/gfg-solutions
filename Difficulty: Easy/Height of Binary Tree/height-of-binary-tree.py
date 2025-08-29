'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if root == None:
            return -1;
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1