class Solution:
    def nonRepeatingChar(self,s):
        n = len(s)
        
        for i in range(n):
            found = False
            
            c = s[i]
            for j in range(n):
                if j == i:
                    continue
                
                if c == s[j]:
                    found = True
                    break
            
            if not found:
                return c
        
        return '$'