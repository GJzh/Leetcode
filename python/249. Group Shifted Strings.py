Solution 1
class Solution(object):
    def getDiff(self, s):
        res = ""
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i-1]) + 26) % 26
            res += (str(diff) + " ")
        return res
        
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        status = {}
        for s in strings:
            key = self.getDiff(s)
            if key not in status:
                status[key] = [s]
            else:
                status[key].append(s)
        res = []
        for key, value in status.items():
            res.append(value)
        return res

Solution 2
class Solution(object):
    class PrefixTree():
        class Node():
            def __init__(self):
                self.next = {}
                self.words = []
            
        def __init__(self, strings):
            self.root = self.Node()
            for s in strings:
                self.addString(s)
            
        def addString(self, s):
            node = self.root
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i-1]) + 26) % 26
                if diff not in node.next:
                    node.next[diff] = self.Node()
                node = node.next[diff]
            node.words.append(s)
            
        def search(self, node, res):
            if node == None: return
            if len(node.words) > 0: res.append(node.words)
            for _, nextNode in node.next.items():
                self.search(nextNode, res)
        
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        tree = self.PrefixTree(strings)
        res = []
        tree.search(tree.root, res)
        return res