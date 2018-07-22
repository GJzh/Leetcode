class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = [[0, 0]]
        hp = [(0, float('inf'))]
        points = sorted([(L, -H, R) for L, R, H in buildings] + [(R, H, None) for L, R, H in buildings])
        
        for x, negH, r in points:
            while x >= hp[0][1]: heapq.heappop(hp)
            if negH < 0:
                heapq.heappush(hp, (negH, r))
            if skyline[-1][1] != -hp[0][0]:
                skyline.append([x, -hp[0][0]])
        return skyline[1:]

