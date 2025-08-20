#User function Template for python3
class Solution:
    def countPairs(self, arr, target):
        k = 0
        
        arr.sort()
        
        # arr = [1 2 2 3 4 5], target = 5
        #        l
        #              r
        
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < target:
                k += right - left
                left += 1
                continue
            
            right -= 1
        
        return k