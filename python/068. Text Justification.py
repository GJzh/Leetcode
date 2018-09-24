class Solution:
    def layout(self, words, n, maxWidth):
        m = len(words)
        # handle the case of one word
        if m == 1:
            res = words[0] + (" " * (maxWidth - len(words[0]) ) )
            return res
        a = (maxWidth - n) // (m-1)
        b = (maxWidth - n) % (m-1)
        res = words[0]
        for i in range(1, b+1):
            res += (" " * (a + 1))
            res += words[i]
        for i in range(b+1, m):
            res += (" " * a)
            res += words[i]
        return res
    
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length = 0
        res = []
        start = 0
        for end in range(len(words)):
            if length + len(words[end]) > maxWidth:
                res.append(self.layout(words[start:end], length - (end - start), maxWidth))
                length = len(words[end]) + 1
                start = end
            else:
                length += len(words[end]) + 1
        last_line = " ".join(words[start:])
        last_line += (" " * (maxWidth - len(last_line)) )
        res.append(last_line)
        return res
