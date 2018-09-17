class Solution(object):
    def findFriends(self, root, visited):
        cur = [root]
        visited[root] = True
        while len(cur) > 0:
            temp = []
            for i in cur:
                for j in range(len(visited)):
                    if self.M[i][j] and i != j and (not visited[j]):
                        temp.append(j)
                        visited[j] = True
            cur = temp
        return
        
        
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.M = M
        n = len(M)
        if not n: return 0
        visited = [False] * n
        cnt = 0
        for i in range(n):
            if visited[i]:
                continue
            # search the friend circle
            self.findFriends(i, visited)
            cnt += 1
        return cnt

