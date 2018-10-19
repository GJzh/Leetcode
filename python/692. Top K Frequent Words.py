class Solution(object):   
    class Element():
        def __init__(self, freq, word):
            self.freq = freq
            self.word = word
            
        def __lt__(self, other):
            if self.freq == other.freq:
                return self.word > other.word
            else:
                return self.freq < other.freq
        
        
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        n = len(words)
        wordFreqs = {}
        for word in words:
            if word not in wordFreqs:
                wordFreqs[word] = 1
            else:
                wordFreqs[word] += 1
        q = []
        for word, freq in wordFreqs.items():
            if len(q) < k:
                heapq.heappush(q, self.Element(freq, word))
            else:
                top = heapq.heappop(q)
                if freq > top.freq:
                    heapq.heappush(q, self.Element(freq, word))
                elif freq == top.freq and word < top.word:
                    heapq.heappush(q, self.Element(freq, word))
                else:
                    heapq.heappush(q, top)
        res = []
        while len(q) > 0:
            res.append(heapq.heappop(q).word)
        return res[::-1]