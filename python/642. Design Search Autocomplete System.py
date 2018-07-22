class AutocompleteSystem:
    class Node:
        def __init__(self):
            self.sentences = collections.defaultdict(int)
            self.next = collections.defaultdict(int)
    
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        n = len(times)
        self.prefix = ""
        self.root = self.Node()
        self.node = self.root
        for i in range(n):
            self.addSentence(sentences[i], times[i])
            
        
    def addSentence(self, sentence, time):
        node = self.root
        for c in sentence:
            if c not in node.next:
                node.next[c] = self.Node()
            node = node.next[c]
            #if sentence not in node.sentences: node.sentences[sentence] = 0
            node.sentences[sentence] += time
                
        

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.addSentence(self.prefix, 1)
            self.prefix = ""
            self.node = self.root
            return []
        else:
            self.prefix += c
            if c not in self.node.next:
                self.node.next[c] = self.Node()
            self.node = self.node.next[c]
            res = []
            cnt = 0
            for sentence, time in sorted(self.node.sentences.items(), key = lambda item: (-item[1], item[0]) ):
                res.append(sentence)
                cnt += 1
                if cnt >= 3: break
            return res

