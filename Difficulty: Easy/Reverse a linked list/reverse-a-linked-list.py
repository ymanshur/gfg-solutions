"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # None<-1<-2  None
        #       p
        #          c
        #             n
        
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            if next == None:
                return curr
            
            prev = curr
            curr = next

        return curr
        