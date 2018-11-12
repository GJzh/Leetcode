Solution 1:
class Solution(object):
    def isSubString(self, word1, word2):
        if len(word1) < len(word2): return False
        idx1, idx2 = 0, 0
        while idx1 < len(word1) and idx2 < len(word2):
            if word1[idx1] == word2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx1 += 1
        return idx2 == len(word2)
    
    
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def Order(word):
            return -len(word), word
        d.sort(key = Order)
        for word in d:
            if self.isSubString(s, word):
                return word
        return ""

Solution 2:
class Solution(object):
    def isSubString(self, word1, word2):
        if len(word1) < len(word2): return False
        idx1, idx2 = 0, 0
        while idx1 < len(word1) and idx2 < len(word2):
            if word1[idx1] == word2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx1 += 1
        return idx2 == len(word2)
    
    
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        candidate = ""
        length = 0
        for word in d:
            if len(word) < length or (len(word) == length and word >= candidate): continue
            if self.isSubString(s, word):
                candidate = word
                length = len(word)
        return candidate

Solution 3:
class Solution(object):    
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        status = {}
        for i in range(len(d)):
            word = d[i]
            if word[0] not in status:
                status[word[0]] = []
            status[word[0]].append((0, i))
        ans = []
        for c in s:
            if c not in status: continue
            cur = status[c]
            del status[c]
            for idx, i in cur:
                if idx == len(d[i])-1:
                    ans.append(d[i])
                else:
                    if d[i][idx+1] not in status:
                        status[d[i][idx+1]] = []
                    status[d[i][idx+1]].append((idx+1, i))
        if len(ans) == 0: return ""
        maxLen = len(max(ans, key = len))
        return min(word for word in ans if len(word) == maxLen)