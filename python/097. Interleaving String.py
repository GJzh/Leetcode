class Solution(object):
    def dfs(self, s1, s2, s3, i, j, visited):
        if i == len(s1) and j == len(s2): return True
        if i < len(s1) and s1[i] == s3[i+j] and (i+1, j) not in visited:
            if self.dfs(s1, s2, s3, i+1, j, visited):
                return True
        if j < len(s2) and s2[j] == s3[i+j] and (i, j+1) not in visited:
            if self.dfs(s1, s2, s3, i, j+1, visited):
                return True
        visited[(i,j)] = True
        return False
            
    
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        visited = {}
        if len(s1) + len(s2) != len(s3): return False
        return self.dfs(s1, s2, s3, 0, 0, visited)