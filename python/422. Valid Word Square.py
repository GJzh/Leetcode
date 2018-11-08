class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m = len(words)
        if m == 0: return True
        n = len(words[0])
        if n == 0: return True
        if m != n: return False
        for i in range(m):
            for j in range(len(words[i])):
                if len(words) <= j or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False
        return True