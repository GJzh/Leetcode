class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        idx = 0
        ans = []
        while idx < n:
            if not s[idx].isdigit():
                ans.append(s[idx])
                idx += 1
                continue
            start = idx
            while idx < n and s[idx].isdigit():
                idx += 1
            num = int(s[start:idx])   
            idx += 1
            cnt = 1
            start = idx
            while idx < n and cnt != 0:
                if s[idx] == "[": cnt += 1
                elif s[idx] == "]": cnt -= 1
                idx += 1
            t = self.decodeString(s[start:idx-1])
            ans.append(t * num)  
        return "".join(ans)