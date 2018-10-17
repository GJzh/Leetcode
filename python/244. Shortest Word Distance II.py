class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.status = {}
        for i in range(len(words)):
            word = words[i]
            if word not in self.status:
                self.status[word] = [i]
            else:
                self.status[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2: return 0
        list1 = self.status[word1]
        list2 = self.status[word2]
        n1 = len(list1)
        n2 = len(list2)
        if n1 == 0 or n2 == 0:
            return float('inf')
        idx1, idx2 = 0, 0
        prev1, prev2 = float('-inf'), float('-inf')
        res = float('inf')
        while idx1 < n1 and idx2 < n2:
            if list1[idx1] < list2[idx2]:
                res = min(res, list1[idx1] - prev2)
                prev1 = list1[idx1]
                idx1 += 1
            else:
                res = min(res, list2[idx2] - prev1)
                prev2 = list2[idx2]
                idx2 += 1
        if idx1 < n1:
            res = min(res, list1[idx1] - prev2)
        else:
            res = min(res, list2[idx2] - prev1)
        return res