Solution 1 (dfs) time: O(k) k is the number of '1's
class Solution(object):
    def dfs(self, image, x, y, visited):
        m = len(image)
        n = len(image[0])
        self.up = min(self.up, x)
        self.down = max(self.down, x)
        self.left = min(self.left, y)
        self.right = max(self.right, y)
        visited[(x,y)] = True
        if x-1 >= 0 and (x-1, y) not in visited and image[x-1][y] == '1': self.dfs(image, x-1, y, visited) 
        if x+1 < m and (x+1, y) not in visited and image[x+1][y] == '1': self.dfs(image, x+1, y, visited) 
        if y-1 >= 0 and (x, y-1) not in visited and image[x][y-1] == '1': self.dfs(image, x, y-1, visited) 
        if y+1 < n and (x, y+1) not in visited and image[x][y+1] == '1': self.dfs(image, x, y+1, visited) 
        return 
    
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0: return 0
        n = len(image[0])
        if n == 0: return 0
        self.left, self.right, self.up, self.down = n-1, 0, m-1, 0
        visited = {}
        self.dfs(image, x, y, visited)
        return (self.right - self.left + 1) * (self.down - self.up + 1)

Solution 2 (dfs) time: O(mlogn + nlogm) k is the number of '1's
class Solution(object):
    def binarySearch(self, image, lowerbound, upperbound, start, end, isHorizontal, searchBlack):
        m = len(image)
        n = len(image[0])
        while lowerbound <= upperbound:
            mid = (lowerbound + upperbound) / 2
            isBlack = False
            for i in range(start, end):
                val = image[i][mid] if isHorizontal else image[mid][i]
                if val == '1':
                    isBlack = True
                    break
            if isBlack == searchBlack:
                upperbound = mid - 1
            else:
                lowerbound = mid + 1
        return lowerbound
    
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0: return 0
        n = len(image[0])
        if n == 0: return 0
        left = self.binarySearch(image, 0, y, 0, m, True, True)
        right = self.binarySearch(image, y+1, n-1, 0, m, True, False)
        up = self.binarySearch(image, 0, x, left, right, False, True)
        down = self.binarySearch(image, x+1, m-1, left, right, False, False)
        return (right - left) * (down - up)