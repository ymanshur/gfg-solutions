class Solution:
    
    def lis(self, arr):
        tmp = []
        
        n = len(arr)    
        for i in range(0, n):
            if len(tmp) == 0:
                tmp.append(arr[i])
                continue
            
            if arr[i] > tmp[-1]:
                tmp.append(arr[i])
                continue
            
            for j in range(0, len(tmp)):
                if tmp[j] >= arr[i]:
                    tmp[j] = arr[i]
                    break
        
        return len(tmp)
       
