# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        status = {}
        visited = {}
        status[node] = UndirectedGraphNode(node.label)
        candidates = [node]
        while len(candidates) > 0:
            temp = []
            for candidate in candidates:
                if candidate not in visited:
                    for neighbor in candidate.neighbors:
                        if neighbor not in status:
                            newNeighbor = UndirectedGraphNode(neighbor.label)
                            status[neighbor] = newNeighbor
                        status[candidate].neighbors.append(status[neighbor])
                    visited[candidate] = True
                    temp += candidate.neighbors
            candidates = temp
        return status[node]
