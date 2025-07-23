class Solution:
    # 1, 2, 3, 4, 5 = ((1 + 5) + (2 + 4) + (3 + 3) + (4 + 2) + (5 + 1)) / 2
    #               = n * (n + 1) / 2
    def findSum(self, n):
        # sum = 0
        # for i in range(1, n + 1):
        #     sum += i
        
        sum = n * (n + 1) // 2
        
        return sum
