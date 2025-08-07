class Solution:
    def sort012(self, arr):
        # _qsort(arr)
        
        # counter = [0] * 3 # 0, 1, 2
        # for i in arr:
        #     counter[i] += 1
        
        # i = 0
        # for x in range(0, len(counter)):
        #     for _ in range(counter[x]):
        #         arr[i] = x
        #         i += 1
        
        # arr = [0, 0, 1, 1, 2, 2]
        #              l              
        #                 r
        #                    i

        n = len(arr)
        i = 0
        l = 0
        r = n - 1
        while i <= r:
            if arr[i] == 0:
                arr[i], arr[l] = arr[l], arr[i]
                l += 1
                i += 1
            elif arr[i] == 1:
                i += 1
            else:
                arr[i], arr[r] = arr[r], arr[i]
                r -= 1
            
            # for x in arr:
            #     print(x, end = " ")
            # print()
        
        
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
        
        
        
    
        
        