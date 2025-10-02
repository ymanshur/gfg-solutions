class Solution:    
    def findUnion(self, a, b):
        st = set(a + b)
        return list(st)
        