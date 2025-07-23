
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        d = a2 - a1
        t = a1
        for i in range(2, n + 1):
            t += d
        return t
