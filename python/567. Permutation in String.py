class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        status = [0] * 26
        if n1 > n2: return False
        for c in s1:
            status[ord(c)-ord('a')] += 1
        left = 0
        for right in range(n2):
            idx = ord(s2[right]) - ord('a')
            status[idx] -= 1
            if status[idx] < 0:
                while(status[idx] < 0):
                    idx2 = ord(s2[left]) - ord('a')
                    status[idx2] += 1
                    left += 1
            elif right - left + 1 == n1:
                return True
        return False

