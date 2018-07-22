class Trie:
    class Node:
        def __init__(self):
            self.next = [None] * 26
            self.isWord = False
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = self.Node()
            cur = cur.next[idx]
        cur.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.next[idx]: return False
            cur = cur.next[idx]
        return cur.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.next[idx]: return False
            cur = cur.next[idx]
        return True

