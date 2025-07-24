#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def numberofElementsInIntersection(self, a, b):
        h = {}
        for x in a:
            h[x] = 1
        
        n = 0
        for x in b:
            if x in h:
                n += 1
                
        return n