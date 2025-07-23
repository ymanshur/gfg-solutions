#User function Template for python3

class Solution:
    def getTable(self,n):
        arr = []
        for i in range(1, 11):
            arr.append(i * n)

        return arr