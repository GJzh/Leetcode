class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        temp = self.countAndSay(n-1)
        cnt = 0
        cur = ord(temp[0]) - ord('0')
        say = ""
        for digit in temp:
            val = ord(digit) - ord('0')
            if val == cur:
                cnt += 1
            else:
                say += str(cnt)
                say += str(cur)
                cur = val
                cnt = 1
        say += str(cnt)
        say += str(cur)
        return say
