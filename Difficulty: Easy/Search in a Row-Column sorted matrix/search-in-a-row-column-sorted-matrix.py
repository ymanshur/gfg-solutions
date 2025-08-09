#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
	    for i in range(len(mat)):
	        for j in range(len(mat[i])):
	            if mat[i][j] == x:
	                return True
		return False
	