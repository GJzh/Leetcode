class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        n = len(S)
        if n == 0:
            return [""]
        c = S[-1]
        res = []
        prefixs = self.letterCasePermutation(S[:n-1])
        if c.isalpha():
            candidates = [c.lower(), c.upper()]
        else:
            candidates = [c]
        for candidate in candidates:
            for prefix in prefixs:
                res.append(prefix + candidate)
        return res
