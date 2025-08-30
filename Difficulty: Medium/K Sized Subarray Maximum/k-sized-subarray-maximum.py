class Solution:
    def maxOfSubarrays(self, arr, k):
        res = []
        
        queue = []
        
        for i in range(0, k):
            while len(queue) > 0 and \
                arr[i] >= arr[queue[-1]]:
                queue.pop()
            
            queue.append(i)
        
        res.append(arr[queue[0]])
        
        n = len(arr)
        for i in range(k, n):
            while len(queue) > 0 and \
                arr[i] >= arr[queue[-1]]:
                queue.pop()
            
            while len(queue) > 0 and \
                queue[0] < i - k + 1:
                queue.pop(0)
            
            queue.append(i)
            res.append(arr[queue[0]])
        
        return res
            