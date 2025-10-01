class Solution:
    def nonRepeatingChar(self, s):
        counter = [0] * 26
        
        for c in s:
            counter[self._indexOf(c)] += 1
                
        for c in s:
            if counter[self._indexOf(c)] == 1:
                return c
        
        return '$'
    
    def _indexOf(self, c):
        return ord(c) - ord('a')
    
    