#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
	    def binarySearch(arr, target):
	        low, high = 0, len(arr) - 1
	        while low <= high:
	            mid = low + (high - low) // 2
	            if arr[mid] == target:
	                return True
	                
	            if arr[mid] > target:
	                high = mid - 1
	            else:
	                low = mid + 1

        # for i in range(len(mat)):
        #     # for j in range(len(mat[i])):
        #     #     if mat[i][j] == x:
        #     #         return True
            
        #     if binarySearch(mat[i], x):
        #         return True
        
        n, m = len(mat), len(mat[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            if mat[i][j] == x:
                return True
            
            if mat[i][j] > x:
                j -= 1
            else:
                i += 1

    	return False
	
	
	