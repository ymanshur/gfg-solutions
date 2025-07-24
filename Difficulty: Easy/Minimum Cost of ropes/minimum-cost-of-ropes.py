import heapq

class Solution:
   def minCost(self, arr):
    min_cost = 0
    
    heapq.heapify(arr) # min-heap
    
    while len(arr) > 1:
        # take most min number from (min-heap) arr
        n1 = heapq.heappop(arr)
        n2 = heapq.heappop(arr)
        
        cost = n1 + n2
        heapq.heappush(arr, cost)
        min_cost += cost
    
    # arr.sort()
    # n = len(arr)
    # for i in range(1, n):
    #     # print("%d %d" % (arr[i - 1], arr[i]))
    #     arr[i] = arr[i - 1] + arr[i] # current cost
    #     min_cost += arr[i]
    #     for j in range(i, n - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    
        
    return min_cost