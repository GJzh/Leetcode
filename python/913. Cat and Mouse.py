from Queue import Queue
from collections import defaultdict
MOUSE, CAT = 1, 2
class Solution(object):      
    
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        states = defaultdict(int)
        outDegree = defaultdict(int)
        q = Queue()
        n = len(graph)
        for i in range(n):
            for j in range(n):
                if j == 0: continue
                if i == 0: 
                    states[(i, j, MOUSE)] = MOUSE
                    states[(i, j, CAT)] = MOUSE
                    q.put((i, j, MOUSE))
                    q.put((i, j, CAT))
                    continue
                if i == j:
                    states[(i, j, MOUSE)] = CAT
                    states[(i, j, CAT)] = CAT
                    q.put((i, j, MOUSE))
                    q.put((i, j, CAT))
                    continue
                outDegree[(i, j, MOUSE)] = len(graph[i])
                for k in graph[j]:
                    if k != 0: outDegree[(i, j, CAT)] += 1
        while q.qsize():
            mPos, cPos, player = q.get()
            if player == MOUSE:
                for prevPos in graph[cPos]:
                    if prevPos == 0: continue
                    if states[(mPos, prevPos, CAT)] != 0: continue
                    if states[(mPos, cPos, player)] == CAT:
                        states[(mPos, prevPos, CAT)] = CAT
                        q.put((mPos, prevPos, CAT))
                    else:
                        outDegree[(mPos, prevPos, CAT)] -= 1
                        if outDegree[(mPos, prevPos, CAT)] == 0:
                            states[(mPos, prevPos, CAT)] = MOUSE
                            q.put((mPos, prevPos, CAT))
            else:
                for prevPos in graph[mPos]:
                    if states[(prevPos, cPos, MOUSE)] != 0: continue
                    if states[(mPos, cPos, player)] == MOUSE:
                        states[(prevPos, cPos, MOUSE)] = MOUSE
                        q.put((prevPos, cPos, MOUSE))
                    else:
                        outDegree[(prevPos, cPos, MOUSE)] -= 1
                        if outDegree[(prevPos, cPos, MOUSE)] == 0:
                            states[(prevPos, cPos, MOUSE)] = CAT
                            q.put((prevPos, cPos, MOUSE))
                
        return states[(1, 2, MOUSE)]