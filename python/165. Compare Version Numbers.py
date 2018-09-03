class Solution(object):
    def findOneNumber(self, version, index):
        n = len(version)
        num = 0
        while index < n and version[index] != '.':
            num = 10 * num + ord(version[index]) - ord("0")
            index += 1
        while index < n and version[index] == '.':
            index += 1
        return num, index
        
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        m = len(version1)
        n = len(version2)
        i, j = 0, 0
        while i < m and j < n:
            num1, i = self.findOneNumber(version1, i)
            num2, j = self.findOneNumber(version2, j)
            if num1 < num2: return -1
            elif num1 > num2: return 1
            else: pass
        while i < m:
            num1, i = self.findOneNumber(version1, i)
            if num1 > 0: return 1
        while j < n:
            num2, j = self.findOneNumber(version2, j)
            if num2 > 0: return -1
        return 0
