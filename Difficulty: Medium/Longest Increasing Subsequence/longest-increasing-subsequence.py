class Solution:
    def search(self, arr, target):
        n = len(arr)
        for i in range(0, n):
            if arr[i] >= target:
                break
        
        return i
        
        
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
            
            j = self.search(tmp, arr[i])
            tmp[j] = arr[i]
        
        return len(tmp)
       
