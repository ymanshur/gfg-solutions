#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        sum = 0
        for i in range(1, number + 1):
            sum += i**2
        
        return sum