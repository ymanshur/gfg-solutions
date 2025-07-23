class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        arr2 = [0] * n
        for i in range(0, n):
            arr2[arr[i] - 1] += 1
        
        m = d = 0
        for i in range(0, n):
            if arr2[i] > 1:
                d = i + 1
            
            if arr2[i] == 0:
                m = i + 1
                
        return [d, m]
                

