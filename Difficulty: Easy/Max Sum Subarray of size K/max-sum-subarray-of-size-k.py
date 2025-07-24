#User function Template for python3
class Solution:
    def maximumSumSubarray (self, arr, k):
        max_sum = 0
        n = len(arr)
        for i in range(min(n, k)):
            max_sum += arr[i]
            
        if n <= k:
            return max_sum
        
        curr_sum = max_sum
        for i in range(k, n):
            curr_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum