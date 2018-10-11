# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
from Queue import Queue
class Solution(object):
    def __init__(self):
        self.Q = Queue()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while not self.Q.empty() and idx < n:
            buf[idx] = self.Q.get()
            idx += 1
        if idx == n: return n
        tempBuf = [None] * 4
        while idx + 4 < n:
            cnt = read4(tempBuf)
            for i in range(cnt):
                buf[idx] = tempBuf[i]
                idx += 1
            if cnt < 4:
                return idx
        cnt = read4(tempBuf)
        for i in range(n - idx, cnt):
            self.Q.put(tempBuf[i])
        for i in range(min(n - idx, cnt)):
            buf[idx] = tempBuf[i]
            idx += 1
        del tempBuf
        return idx