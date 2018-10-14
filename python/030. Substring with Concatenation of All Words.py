class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        if n == 0: return []
        if len(words) == 0: return []
        length = len(words[0])
        if length == 0: return []
        # get frequencies
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        res = []
        
        for start in range(length):
            left, right = start, start
            cnt = len(words)
            tempFreq = {}
            while right <= n - length:
                t = s[right:right+length]
                if t in freq:
                    if t in tempFreq:
                        tempFreq[t] += 1  
                    else:
                        tempFreq[t] = 1
                    if freq[t] - tempFreq[t] >= 0:
                        cnt -= 1
                    else:
                        while freq[t] < tempFreq[t]:
                            word = s[left:left+length]
                            tempFreq[word] -= 1
                            if tempFreq[word] < freq[t]:
                                cnt += 1
                            left += length
                    if cnt == 0:
                        res.append(left)
                        word = s[left:left+length]
                        tempFreq[word] -= 1
                        cnt += 1
                        left += length
                        
                else:
                    tempFreq = {}
                    left = right + length
                    cnt = len(words)
                    
                
                
                right = right + length
        return res