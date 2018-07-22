class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        n = len(source)
        i = j = 0
        cur = ""
        while i < n:
            idx1 = source[i].find("/*", j)
            idx2 = source[i].find("//", j)
            # no comment
            if idx1 == -1 and idx2 == -1:
                cur += source[i][j:]
                if len(cur) > 0: res.append(cur)
                cur = ""
                i += 1
                j = 0
            # block comment
            elif idx1 >= 0 and (idx1 < idx2 or idx2 == -1):
                cur += source[i][j:idx1]
                j = idx1+2
                while i < n and source[i].find("*/", j) == -1:
                    i += 1
                    j = 0
                j = source[i].find("*/", j) + 2
                if j == len(source[i]):
                    if len(cur) > 0: res.append(cur)
                    cur = ""
                    i += 1
                    j = 0
            # line comment
            else:
                cur += source[i][j:idx2]
                if len(cur) > 0: res.append(cur)
                cur = ""
                i += 1
                j = 0
        return res

