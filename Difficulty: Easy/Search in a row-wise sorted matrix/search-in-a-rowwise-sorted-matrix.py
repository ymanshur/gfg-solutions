
#User function Template for python3

class Solution:
    # Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x):
        for i in range(len(mat)):
            j = self.binsect(mat[i], x)
            if j > -1:
                return True
        
    	return False 
    	
    def binsect(self, arr, x):
        lo, hi = 0, len(arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] == x:
                return mid
            
            if arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return -1
