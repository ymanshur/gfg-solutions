class Solution:
    def findPermutation(self, s):
        # let unordered set, ensure all permutations are unique
        res = set()
        
        n = len(s)
        
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
                
        used = [False] * n
        arr = []
        
        permute(arr, 0)
            
        return list(res)
        
        
        
        
        
