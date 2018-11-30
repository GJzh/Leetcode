time: O((n-m+1)^2 * m), space: O(n)
class Solution(object):
    def isValid(self, s, t):
        idx = 0
        while idx < len(s):
            if s[idx] == "?" or s[idx] == t[idx]:
                idx += 1
            else:
                return False
        return True
    
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        ans = []
        m = len(stamp)
        n = len(target)
        marks = "?" * m
        final = "?" * n
        visited = [False] * (n - m + 1)
        cnt = 0
        while cnt < n - m + 1:
            flag = False
            for i in range(n - m + 1):
                if not visited[i] and self.isValid(target[i:i+m], stamp):
                    visited[i] = True
                    ans.append(i)
                    target = target[:i] + marks + target[i+m:]
                    flag = True
                    break
            if target == final or flag == False: break
        return ans[::-1] if target == final else []