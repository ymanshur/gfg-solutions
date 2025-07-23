
class Solution:
    """
    d = a2 - a1
    t1 = a1 + (i - 1) * d
    t2 = a1 + (i - 2) * d
    t3 = a1 + (i - 3) * d
    tn = a1 + (n - 1) * d
    """
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        d = a2 - a1
        # tn = a1
        # for i in range(1, n):
        #     tn += d
        return a1 + (n - 1) * d
