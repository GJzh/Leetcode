class Solution(object):
    def translate(self, word):
        if len(word) == 0: return []
        prev = word[0]
        ans = []
        start, idx = 0, 1
        while idx < len(word):
            if word[idx] != prev:
                ans.append((prev, idx - start))
                start = idx
                prev = word[idx]
            idx += 1
        ans.append((prev, idx - start))
        return ans
         
    def stretchy(self, reference, word):
        idx = 0
        pos = 0
        while idx < len(word):
            cur = word[idx]
            if pos == len(reference) or reference[pos][0] != cur: return False
            k = 0
            while idx <  len(word) and word[idx] == cur:
                idx += 1
                k += 1
            if (reference[pos][1] < 3 and reference[pos][1] != k) or (reference[pos][1] >= 3 and k > reference[pos][1]):
                return False
            pos += 1
        return pos == len(reference)
            
        
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        reference = self.translate(S)
        cnt = 0
        for word in words:
            if self.stretchy(reference, word):
                cnt += 1
        return cnt