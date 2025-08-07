class Solution:
    def sort012(self, arr):
        counter = [0] * 3 # 0, 1, 2
        for i in arr:
            counter[i] += 1
        
        i = 0
        while i < len(arr):
            for x in range(0, len(counter)):
                for _ in range(counter[x]):
                    arr[i] = x
                    i += 1
         
        
        # _qsort(arr)
        
    def _qsort(self, arr, low=0, high=None):
        if high == None:
            high = len(arr) - 1
        
        if low < high:
            pi = qsort_partition(arr, low, high)
            qsort(arr, low, pi - 1)
            qsort(arr, pi + 1, high)
    
    def _qsort_partition(self, arr, low, high):
        pivot = arr[high]
        
        l = low - 1
        for r in range(low, high):
            if arr[r] < pivot:
                l += 1
                arr[l], arr[r] = arr[r], arr[l]
        
        arr[l + 1], arr[high] = arr[high], arr[l + 1]
        return l + 1
        
        
        
    
        
        