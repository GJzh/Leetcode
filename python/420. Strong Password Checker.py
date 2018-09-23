class Solution:
    def threeCharacters(self, s):
        cnt = 0
        status = [False] * 3
        for c in s:
            if c.isdigit():
                status[0] = True
            if c.isupper():
                status[1] = True
            if c.islower():
                status[2] = True
            if status[0] and status[1] and status[2]:
                break
        for i in status:
            if i: cnt += 1
        return 3 - cnt
    
    def repeatedCharacters(self, s):
        repeats = [[], [], []]
        num = 0
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                if cnt >= 3:
                    repeats[cnt%3].append(cnt)
                    num += cnt // 3
                cnt = 1
            
        if cnt >= 3:
            repeats[cnt%3].append(cnt)
            num += cnt // 3
        return repeats, num
    
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 6
        # add or replace
        x = self.threeCharacters(s)
        # delete or replace
        repeats, y = self.repeatedCharacters(s)

        if n < 6:
            z = 6 - n
            if len(repeats[2]) > 0:
                return max(2, x)
            else:
                return max(z, x)
        elif n > 20:
            i, j, k = 0, 0, 0
            z = n - 20
            while i < len(repeats[0]) and z:
                if repeats[0][i] > 3:
                    repeats[2].append(repeats[0][i]-1)
                y -= 1
                z -= 1
                i += 1
            while j < len(repeats[1]) and z >= 2:
                if repeats[1][j] > 4:
                    repeats[2].append(repeats[1][j]-2)
                y -= 1
                z -= 2
                j += 1
            while k < len(repeats[2]) and z >= 3:
                y -= min(z//3, repeats[2][k]//3)
                z -= repeats[2][k] // 3 * 3
                k += 1
            return (n - 20) + max(x, y)
        else:
            return max(x, y)
