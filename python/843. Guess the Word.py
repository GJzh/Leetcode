# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def match(self, word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt += 1
        return cnt
    
    def shrinkWordlist(self, wordlist, guessWord, matches):
        ans = []
        for word in wordlist:
            if self.match(word, guessWord) == matches:
                ans.append(word)
        return ans
    
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        for i in range(10):
            guessWord = wordlist[random.randint(0, len(wordlist)-1)]
            matches = master.guess(guessWord)
            if matches == 6: break
            wordlist = self.shrinkWordlist(wordlist, guessWord, matches)
        return