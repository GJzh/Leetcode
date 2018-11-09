class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        cnt1 = cnt2 = 0
        status = {}
        for i in range(n):
            if secret[i] == guess[i]: cnt1 += 1
            if secret[i] not in status: status[secret[i]] = 0
            if guess[i] not in status: status[guess[i]] = 0
            if status[secret[i]] >= 0: 
                cnt2 += 1
            else:
                cnt2 -= 1
            status[secret[i]] += 1
            if status[guess[i]] <= 0: 
                cnt2 += 1
            else:
                cnt2 -= 1
            status[guess[i]] -= 1 
        return str(cnt1) + "A" + str(n - cnt1 - cnt2 / 2) + "B"