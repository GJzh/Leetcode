class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        n = len(word)
        m = len(abbr)
        if n == 0:
            return abbr == '0'
        idx1, idx2 = 0, 0
        while idx1 < n and idx2 < m:
            if abbr[idx2].isalpha():
                if word[idx1] == abbr[idx2]:
                    idx1 += 1
                    idx2 += 1
                else:
                    return False
            elif abbr[idx2] == "0":
                return False
            else:
                val = ""
                while idx2 < m and abbr[idx2].isdigit():
                    val += abbr[idx2]
                    idx2 += 1
                
                idx1 += int(val)
            
        return idx1 == n and idx2 == m