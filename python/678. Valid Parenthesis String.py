class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftPare = []
        stars = []
        for i in range(len(s)):
            if s[i] == "(":
                leftPare.append(i)
            elif s[i] == ")":
                if len(leftPare) > 0:
                    leftPare.pop()
                elif len(stars) > 0:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        if len(leftPare) == 0: return True
        if len(leftPare) > len(stars): return False
        while len(leftPare) > 0:
            if stars[-1] < leftPare[-1]:
                return False
            else:
                leftPare.pop()
                stars.pop()
        return True