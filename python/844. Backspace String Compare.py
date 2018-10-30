class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        m, n = len(S), len(T)
        idx1, idx2 = m-1, n-1
        while idx1 >= 0 or idx2 >= 0:
            cnt1 = 0
            while idx1 >= 0:
                if S[idx1] == '#':
                    cnt1 -= 1
                else:
                    cnt1 += 1
                if cnt1 > 0: break
                idx1 -= 1
            cnt2 = 0
            while idx2 >= 0:
                if T[idx2] == '#':
                    cnt2 -= 1
                else:
                    cnt2 += 1
                if cnt2 > 0: break
                idx2 -= 1
            if idx1 < 0 and idx2 < 0: return True
            elif idx1 < 0 or idx2 < 0: return False
            elif S[idx1] != T[idx2]: return False
            idx1 -= 1
            idx2 -= 1
        
        return True