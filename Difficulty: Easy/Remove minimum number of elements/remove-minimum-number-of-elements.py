class Solution:
    def minRemove(self, arr1, arr2):
        freq1 = {}
        for x in arr1:
            if x not in freq1:
                freq1[x] = 1
                continue
            
            freq1[x] += 1
        
        freq2 = {}
        for x in arr2:
            if x not in freq2:
                freq2[x] = 1
                continue
            
            freq2[x] += 1
        
        min_remove = 0
        for x in freq1:
            if x not in freq2:
                continue
            
            # print("%d %d %d" % (x, freq1[x], freq2[x]))
            min_remove += min(freq1[x], freq2[x])
        
        return min_remove