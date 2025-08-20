# User function Template for python3

class Solution:
    def findEquilibrium(self, arr):
        # arr[]        = [1, 2, 0, 3]
        # arrPreSum[]  = [1, 3, 3, 6]
        # arrPostSum[] = [6, 5, 3, 3]
        # res          =        i
        
        n = len(arr)
        arrPreSum = [0] * n
        arrPreSum[0] = arr[0]
        for i in range(1, n):
            arrPreSum[i] = arrPreSum[i - 1] + arr[i]
        
        arrPostSum = [0] * n
        arrPostSum[n - 1] = arr[n - 1]
        for i in range(n - 2, 0, -1):
            arrPostSum[i] = arr[i] + arrPostSum[i + 1]
        
        for i in range(n):
            if arrPreSum[i] == arrPostSum[i]:
                return i
        
        return -1