class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 0: return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        if n == 0: return []
        status = {}
        for i in range(n):
            status[words[i][::-1]] = i
        pairs = set()
        for i in range(n):
            word = words[i]
            for j in range(len(word)+1):
                left = word[:j]
                right = word[j:]
                # other|left|right
                if self.isPalindrome(left) and right in status and status[right] != i:
                    pairs.add((status[right], i))
                # left|right|other
                if self.isPalindrome(right) and left in status and status[left] != i:
                    pairs.add((i, status[left]))
        res = []
        for i, j in list(pairs):
            res.append([i,j])
        return res