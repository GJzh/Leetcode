class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        visited = {}
        res = ""
        for s in S:
            for t in T:
                if s == t:
                    res += t
                    visited[s] = True
        for t in T:
            if t not in visited:
                res += t
        return res