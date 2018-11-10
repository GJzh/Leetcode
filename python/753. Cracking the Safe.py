Solution 1: DFS, time: O(k ** (n+1)), space: O(k ** n)       
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

Solution 2: (Lyndon Word) time: O(k ** n), space: O(k ** n)       
class Solution(object):
    def crackSafe(self, n, k):
        M = k**(n-1)
        P = [i*k+j for j in range(k) for i in range(M)]
        ans = []

        for i in range(k**n):
            j = i
            while P[j] >= 0:
                ans.append(str(j / M))
                P[j], j = -1, P[j]

        return "".join(ans) + "0" * (n-1)