class Solution(object):
    def dfs(self, maze, cur, destination):
        if cur == destination: return True
        m = len(maze)
        n = len(maze[0])
        for direction in self.directions:
            x, y = cur
            while x >= 0 and x < m and y >= 0 and y < n and maze[x][y] != 1:
                x += direction[0]
                y += direction[1]
            x -= direction[0]
            y -= direction[1]
            if (x,y) not in self.visited:
                self.visited[(x,y)] = True
                if self.dfs(maze, [x,y], destination):
                    return True
        return False
    
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m = len(maze)
        if m == 0: return False
        n = len(maze[0])
        if n == 0: return False
        self.visited = {}
        self.directions = [[-1, 0],[1, 0],[0, -1],[0, 1]]
        return self.dfs(maze, start, destination)  