class Solution:
    def findPermutation(self, s):
        # let unordered set, ensure all permutations are unique
        
        res = set() # nPr ~= n! 
        
        n = len(s)
        used = [False] * n
        
        def permute(arr, i):
            if i == n:
                res.add("".join(arr))
                return
            
            for j in range(0, n):
                if used[j]:
                    continue
                
                used[j] = True
                arr.append(s[j])
                
                permute(arr, i + 1)
                
                used[j] = False
                arr.pop()
                
        arr = []
        
        permute(arr, 0)
        
        # Time complexity:
        #   Total operation during permutation generation ~= O(n!)  
        # Auxiliary space:
        #   Total length of res, used, and arr = n! + n + n ~= O(n!)
            
        return list(res)
        
        
        
        
        
