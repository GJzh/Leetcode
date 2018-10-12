class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if n == 0: return []
        res = [0] * n
        q = []
        prev = 0
        for log in logs:
            idx, key, time = log.split(":")
            idx = int(idx)
            time = int(time)
            if key == "start":
                if len(q) != 0:
                    res[q[-1]] += (time - prev)
                q.append(idx)
                prev = time
            else:
                res[idx] += (time - prev + 1)   
                q.pop()
                prev = time + 1
        return res