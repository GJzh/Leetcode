class Solution(object):
    def wordsAbbreviation(self, words):
        def abbrev(word, i = 0):
            if len(word) - i <= 3: return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]
        
        n = len(words)
        prefix = [0] * n
        ans = map(abbrev, words)
        for i in range(n):
            while True:
                dupes = []
                for j in range(i+1, n):
                    if ans[j] == ans[i]:
                        dupes.append(j)
                if len(dupes) == 0: break
                dupes.append(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])
        return ans