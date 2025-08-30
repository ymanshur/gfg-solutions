from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        res = []
        
        dq = deque()
        
        for i in range(0, k):
            while len(dq) > 0 and \
                arr[i] >= arr[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        res.append(arr[dq[0]])
        
        n = len(arr)
        for i in range(k, n):
            while len(dq) > 0 and \
                arr[i] >= arr[dq[-1]]:
                dq.pop()
            
            while len(dq) > 0 and \
                dq[0] < i - k + 1:
                dq.popleft()
            
            dq.append(i)
            res.append(arr[dq[0]])
        
        return res
            