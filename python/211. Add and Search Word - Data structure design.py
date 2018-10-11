class WordDictionary(object):
    class Node():
        def __init__(self):
            self.next = [None] * 26
            self.isWord = False
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if node.next[idx] == None:
                node.next[idx] = self.Node()
            node = node.next[idx]
        node.isWord = True

    def dfs(self, node, word, k):
        if node == None: return False
        if k == len(word):
            return node.isWord
        if word[k] != '.':
            idx = ord(word[k])-ord('a')
            return self.dfs(node.next[idx], word, k+1)
        else:
            for i in range(26):
                if self.dfs(node.next[i], word, k+1):
                    return True
            return False
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word, 0)