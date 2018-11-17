from collections import defaultdict
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbreviations = defaultdict(int)
        self.words = {}
        for word in dictionary:
            if word in self.words: continue
            self.words[word] = True
            key = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
            self.abbreviations[key] += 1

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        key = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        return key not in self.abbreviations or (self.abbreviations[key] == 1 and word in self.words)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)