class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0: return []
        m = len(words[0])
        freq = {}
        for word in words:
            if word not in freq: freq[word] = 0
            freq[word] += 1
        total = len(freq)
        ans = []
        for offset in range(m):
            status = {}
            start = end = offset
            cnt = total
            while end + m <= len(s):
                word = s[end:end+m]
                if word not in freq:
                    status = {}
                    cnt = total
                    start = end = end + m
                else:
                    if word not in status:
                        status[word] = 1
                    else:
                        status[word] += 1
                    if status[word] == freq[word]:
                        cnt -= 1
                        if cnt == 0: 
                            ans.append(start)
                            status[s[start:start+m]] -= 1
                            start += m
                            cnt += 1
                    elif status[word] > freq[word]:
                        while status[word] > freq[word]:
                            prevWord = s[start:start+m]
                            if status[prevWord] == freq[prevWord]: cnt += 1
                            status[prevWord] -= 1
                            start += m
                    else:
                        pass
                    end += m
        return ans