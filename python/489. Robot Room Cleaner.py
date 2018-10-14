class Solution(object):
    def goBack(self, robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            
    def dfs(self, robot, pos, d):

        robot.clean()
        
        for _ in range(4):
            newPos = (pos[0] + self.directions[d][0], pos[1] + self.directions[d][1])
            if newPos not in self.visited and robot.move():
                self.visited[pos] = True
                self.dfs(robot, newPos, d)
                self.goBack(robot)
            robot.turnRight()
            d = (d + 1) % 4
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = {}
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.dfs(robot, (0, 0), 0)