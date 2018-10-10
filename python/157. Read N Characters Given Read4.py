# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        length = 0
        tempBuf = [None] * 4
        idx = 0
        while idx+4 < n:
            cnt = read4(tempBuf)
            for i in range(cnt):
                buf[idx] = tempBuf[i]
                idx += 1
            if cnt < 4:
                return idx
        cnt = read4(tempBuf)
        for i in range(min(n - idx, cnt)):
            buf[idx] = tempBuf[i]
            idx += 1
        return idx