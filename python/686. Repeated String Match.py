class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        ans * len(A) >= len(B) > (ans-2) * len(A)
        len(B)/len(A) <= ans < len(B)/len(A) + 2, len(B)/len(A) is float
        """
        K = int(math.ceil(1.0 * len(B) / len(A)))
        for k in range(K, K+2):
            candidate = A * k
            if B in candidate:
                return k
        return -1