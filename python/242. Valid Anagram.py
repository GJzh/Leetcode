class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        if n != m: return False
        status = [0] * 26
        for c in s:
            status[ord(c)- ord('a')] += 1
        for c in t:
            status[ord(c)- ord('a')] -= 1
            if status[ord(c)- ord('a')] < 0:
                return False
        return True
