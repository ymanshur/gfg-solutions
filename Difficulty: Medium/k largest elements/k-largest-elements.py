import heapq

class Solution:
	def kLargest(self, arr, k):
	    max_heap = []
		for x in arr:
		    heapq.heappush(max_heap, -x)
		
		max_arr = []
		for i in range(0, k):
		    x = -heapq.heappop(max_heap)
		    max_arr.append(x)
		
		return max_arr
		    