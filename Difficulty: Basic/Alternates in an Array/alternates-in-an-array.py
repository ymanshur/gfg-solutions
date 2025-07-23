class Solution:
    def getAlternates(self, arr):
        arr2 = []
        for i in range(0, len(arr)):
            if (i + 1) % 2 == 0:
                continue
            
            arr2.append(arr[i])
            
        return arr2