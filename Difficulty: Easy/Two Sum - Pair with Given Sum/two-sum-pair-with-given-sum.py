class Solution:
	def twoSum(self, arr, target):
		hash = {}
		for i, x in enumerate(arr):
		    hash[x] = i
		
		for i, x in enumerate(arr):
		    comp = target - x
		    if comp in hash and hash[comp] != i:
		        return True
	    
	    return False