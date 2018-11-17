class Solution(object):
    def helper(self, accounts, start, num):
        ans = float('inf')
        while start < len(accounts) and accounts[start] == 0:
            start += 1
        prev = 0
        for i in range(start+1, len(accounts)):
            if accounts[i] != prev and (accounts[start] * accounts[i] < 0):
                accounts[i] += accounts[start]
                ans = min(ans, self.helper(accounts, start + 1, num + 1))
                accounts[i] -= accounts[start]
                prev = accounts[i]
        return ans if ans != float('inf') else num
    
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        users = {}
        for x, y, z in transactions:
            if x not in users: users[x] = 0
            if y not in users: users[y] = 0
            users[x] += z
            users[y] -= z
        accounts = []
        for user, money in users.items():
            if money != 0:
                accounts.append(money)
        del users
        return self.helper(accounts, 0, 0)