class Solution:
    def countFreq(self, arr, target):
        # count = 0
        # for x in arr:
        #     if x == target:
        #         count += 1
        
        # arr = [1, 1, 2, 2, 2, 2, 3]
        #              l
        #           h
        #              l2
        #                       h2
        
        l = l2 = 0
        h = len(arr) - 1
        while l <= h:
            m = l + ((h - l) >> 1)
            if arr[m] >= target:
                h = m - 1
                l2 = m
            else:
                l = m + 1
        
        if arr[l2] != target:
            return 0
    
        l = l2
        h = h2 = len(arr) - 1
        while l <= h:
            m = l + ((h - l) >> 1)
            if arr[m] <= target:
                l = m + 1
                h2 = m
            else:
                h = m - 1
        
        
        return h2 - l2 + 1
            
        