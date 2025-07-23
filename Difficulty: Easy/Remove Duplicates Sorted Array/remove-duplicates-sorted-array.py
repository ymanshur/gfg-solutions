class Solution:
    def removeDuplicates(self, arr):
        curr = arr[0]
        arr2 = [curr]
        for x in arr:
            if x == curr:
                continue
            
            curr = x
            arr2.append(curr)
        
        return arr2