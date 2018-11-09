class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        m = len(start)
        n = len(end)
        start = list(start)
        end = list(end)
        if m != n: return False
        for i in range(n):
            if start[i] == end[i]: continue
            if end[i] == 'X':
                if start[i] == 'L': return False
                j = i
                while j < n and start[j] == 'R':
                    j += 1
                if j < n and start[j] == 'X':
                    start[i], start[j] = start[j], start[i]
                else:
                    return False
            elif end[i] == 'L':
                if start[i] == 'R': return False
                j = i
                while j < n and start[j] == 'X':
                    j += 1
                if j < n and start[j] == 'L':
                    start[i], start[j] = start[j], start[i]
                else:
                    return False
            else:
                return False
        return True