class Solution:
    def search(self, arr, target):
        index = 0
        
        low = 0
        high = len(arr)
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == target:
                return mid
            
            if arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return low
        
        
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
       
