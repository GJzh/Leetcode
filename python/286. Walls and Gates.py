class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if  m == 0: return
        n = len(rooms[0])
        if  n == 0: return
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        distance = 1
        while len(q):
            temp = []
            for x, y in q:
                if x-1 >= 0 and rooms[x-1][y] == 2147483647:
                    rooms[x-1][y] = distance
                    temp.append((x-1,y))
                if x+1 < m and rooms[x+1][y] == 2147483647:
                    rooms[x+1][y] = distance
                    temp.append((x+1,y))
                if y-1 >= 0 and rooms[x][y-1] == 2147483647:
                    rooms[x][y-1] = distance
                    temp.append((x,y-1))
                if y+1 < n and rooms[x][y+1] == 2147483647:
                    rooms[x][y+1] = distance
                    temp.append((x,y+1))
            q = temp
            distance += 1
        return