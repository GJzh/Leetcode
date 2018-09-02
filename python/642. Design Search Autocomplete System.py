class AutocompleteSystem(object):
    class Node(object):
        def __init__(self):
            self.sentences = {}
            self.next = {}
    
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = self.Node()
        for i in range(len(sentences)):
            self.addSentence(sentences[i], times[i])
        self.prefix = ""
        self.cur = self.root
        
    def addSentence(self, sentence, time):
        node = self.root
        for c in sentence:
            if c not in node.next:
                node.next[c] = self.Node()
            node = node.next[c]
            if sentence not in node.sentences:
                node.sentences[sentence] = 0
            node.sentences[sentence] += time
            

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.addSentence(self.prefix, 1)
            self.cur = self.root
            self.prefix = ""
            return []
        else:
            self.prefix += c
            if c not in self.cur.next:
                self.cur.next[c] = self.Node()
            self.cur = self.cur.next[c]
            return self.pickTop3()
        
    def pickTop3(self):
        if len(self.cur.sentences) == 0:
            return []
        cnt = 0
        res = []
        for sentence, time in sorted(self.cur.sentences.items(), key = self.findNum):
            res.append(sentence)
            cnt += 1
            if cnt >= 3:
                break
        return res
        
        
    def findNum(self, item):
        return (-item[1], item[0])
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
