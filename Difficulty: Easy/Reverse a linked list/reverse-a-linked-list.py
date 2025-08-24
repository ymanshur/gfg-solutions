"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        stack = []
        
        curr = head
        while curr.next:
            stack.append(curr)
            curr = curr.next
        
        head = curr
        
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None

        return head
        