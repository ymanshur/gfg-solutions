class Solution:
    def leaders(self, arr):
        n = len(arr)
        leader = arr[n - 1]
        arr2 = [leader]
        for i in range(n - 2, -1, -1):
            if arr[i] >= leader:
                leader = arr[i]
                arr2.append(leader)

        return arr2[::-1]