class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dictionary = {}
        ans = ["0"] * (n-1)
        for i in range(k ** n + 1):
            cur = "".join(ans[len(ans)-n+1:])
            for j in range(k-1, -1, -1):
                if cur + str(j) not in dictionary:
                    dictionary[cur + str(j)] = True
                    ans.append(str(j))
                    break
        return "".join(ans)
        