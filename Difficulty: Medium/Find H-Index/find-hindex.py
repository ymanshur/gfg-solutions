class Solution:
    def hIndex(self, citations):
        n = len(citations)
        freq = [0] * (n + 1)
        
        for i in range(n):
            citation = citations[i]
            if citation > n:
                freq[n] += 1
            else:
                freq[citations[i]] += 1
        
        cnt = freq[n]
        i = n
        while i > -1:
            if cnt >= i:
                return i

            i -= 1
            cnt += freq[i]

        return 0 