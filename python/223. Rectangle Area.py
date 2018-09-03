class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = 0
        area += (C-A) * (D-B)
        area += (G-E) * (H-F)
        a = b = 0
        if not (C <= E or G <= A):
            a = min(C,G) - max(A,E)
        if not (D <= F or H <= B):
            b = min(D,H) - max(B,F)
        area -= a * b
        return area
