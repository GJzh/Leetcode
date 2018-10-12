from Queue import Queue
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        if n == 0: return ""
        if n == 1: return words[0]
        indegrees = {}
        graph = {}
        for word in words:
            for c in word:
                indegrees[c] = 0
                graph[c] = set()
        # build the graph
        prevWord = words[0]
        for i in range(1, n):
            curWord = words[i]
            for j in range(min(len(prevWord), len(curWord))):
                if prevWord[j] == curWord[j]: continue
                if curWord[j] not in graph[prevWord[j]]:
                    indegrees[curWord[j]] += 1
                    graph[prevWord[j]].add(curWord[j])
                break
            prevWord = curWord
        # order
        res = ""
        q = Queue()
        # find zero degree characters
        for c, indegree in indegrees.items():
            if indegree == 0:
                q.put(c)
        while q.qsize() > 0:
            cur = q.get()
            res += cur
            for neighbour in graph[cur]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    q.put(neighbour)
        if len(res) == len(indegrees):
            return res
        else:
            return ""