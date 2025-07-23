class Solution:
    def binarysearch(self, arr, k):
        n = len(arr)
        
        l = 0
        h = n - 1
        i = h
        while l <= h:
            m = l + (h - l) // 2
            # print("%d %d %d" % (arr[l], arr[m], arr[h]))
            if arr[m] == k:
                i = m   
                h = m - 1
            elif arr[m] > k:
                h = m - 1
            else:
                l = m + 1
                
        if arr[i] == k:
            return i
        
        return -1
        