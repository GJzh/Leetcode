class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if len(sentence[0]) > cols: return 0
        sentenceWithSpace = " ".join(sentence) + " "
        n = len(sentenceWithSpace)
        start = 0
        for _ in range(rows):
            start += cols
            while sentenceWithSpace[start % n] != " ":
                start -= 1
            start += 1
        return start / n