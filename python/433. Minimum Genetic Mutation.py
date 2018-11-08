class Solution(object):
    def isValidMutation(self, s, t):
        i = 0
        cnt = 0
        while i < 8:
            if s[i] != t[i]: cnt += 1
            if cnt > 1: return False
            i += 1
        return True
    
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        visited = {}
        cur = [start]
        cnt = 0
        while len(cur):
            temp = []
            cnt += 1
            for word1 in cur:
                for word2 in bank:
                    if word2 not in visited and self.isValidMutation(word1, word2):
                        visited[word2] = True
                        temp.append(word2)
                        if word2 == end: return cnt
            cur = temp
        return -1