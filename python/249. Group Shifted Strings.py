class Solution(object):
    def getDiff(self, s):
        res = ""
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i-1]) + 26) % 26
            res += (str(diff) + " ")
        return res
        
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        status = {}
        for s in strings:
            key = self.getDiff(s)
            if key not in status:
                status[key] = [s]
            else:
                status[key].append(s)
        res = []
        for key, value in status.items():
            res.append(value)
        return res