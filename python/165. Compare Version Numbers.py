class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(version1) and j < len(version2):
            num1 = num2 = 0
            while i < len(version1) and version1[i] != '.':
                num1 = 10 * num1 + ord(version1[i]) - ord('0')
                i += 1
            while j < len(version2) and version2[j] != '.':
                num2 = 10 * num2 + ord(version2[j]) - ord('0')
                j += 1
            if num1 < num2: return -1
            elif num1 > num2: return 1
            else: pass
            while i < len(version1) and version1[i] == '.': i += 1
            while j < len(version2) and version2[j] == '.': j += 1
        # process the residual tail, if the numbers in residual are 0s, we should return 0
        if i < len(version1): 
            num1 = 0
            while i < len(version1):
                while i < len(version1) and version1[i] != '.':
                    num1 = 10 * num1 + ord(version1[i]) - ord('0')
                    i += 1
                if num1 > 0: return 1
                while i < len(version1) and version1[i] == '.': i += 1
            return 0 
        elif j < len(version2):
            num2 = 0
            while j < len(version2):
                while j < len(version2) and version2[j] != '.':
                    num2 = 10 * num2 + ord(version2[j]) - ord('0')
                    j += 1
                if num2 > 0: return -1
                while j < len(version2) and version2[j] == '.': j += 1
            return 0
        else: return 0

