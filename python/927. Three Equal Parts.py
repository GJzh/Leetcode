class Solution(object):
    def isValid(self, A, i1, i2, i3, length):
        for k in range(length):
            if A[i1+k] != A[i2+k] or A[i1+k] != A[i3+k]:
                return False
        return True
    
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) < 3: return [-1, -1]
        cnt = 0
        for a in A:
            if a == 1: cnt += 1
        if cnt % 3 != 0: return [-1, -1]
        if cnt == 0: return [0,2]
        sz = cnt / 3
        cnt = 0
        for idx in range(len(A)):
            if A[idx] == 1: 
                cnt += 1
                if cnt == 1: i1 = idx
                if cnt == sz: j1 = idx
                if cnt == sz + 1: i2 = idx
                if cnt == 2 * sz: j2 = idx
                if cnt == 2 * sz + 1: i3 = idx
                if cnt == 3 * sz: j3 = idx
        zeros = len(A) - j3 - 1
        j1 += zeros
        j2 += zeros
        j3 += zeros
        if j1 >= i2 or j2 >= i3 or (j1 - i1) != (j2 - i2) or (j1 - i1) != (j3 - i3): return [-1, -1]
        if self.isValid(A, i1, i2, i3, j1-i1):
            return [j1, j2 + 1]
        else:
            return [-1, -1]