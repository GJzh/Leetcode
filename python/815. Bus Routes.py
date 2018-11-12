class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        stops = {}
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in stops:
                    stops[stop] = []
                stops[stop].append(i)
        if S not in stops or T not in stops: return -1
        visitedStops = {}
        visitedBuses = {}
        cnt = 0
        q = [S]
        while len(q):
            cnt += 1
            buses = []
            for stop in q:
                for bus in stops[stop]:
                    if bus not in visitedBuses:
                        visitedBuses[bus] = True
                        buses.append(bus)
            q = []
            for bus in buses:
                for stop in routes[bus]:
                    if stop not in visitedStops:
                        visitedStops[stop] = True
                        q.append(stop)
                        if stop == T: return cnt
        return -1