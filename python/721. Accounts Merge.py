class Solution(object):
    class UnionFind():
        def __init__(self, n):
            self.users = [k for k in range(n)]
            self.sz = [1] * n
        
        def find(self, k):
            while self.users[k] != k:
                self.users[k] = self.users[self.users[k]]
                k = self.users[k]
            return k
        
        def merge(self, k1, k2):
            k1 = self.find(k1)
            k2 = self.find(k2)
            if k1 == k2: return k1
            if self.sz[k1] < self.sz[k2]:
                self.users[k1] = k2
                self.sz[k2] += self.sz[k1]
                return k2
            else:
                self.users[k2] = k1
                self.sz[k1] += self.sz[k2]
                return k1
    
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        emails = {}
        p = self.UnionFind(n)
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in emails:
                    emails[email] = i
                else:
                    emails[email] = p.merge(i, emails[email])
        persons = {}
        for email, accoundId in emails.items():
            personID = p.find(accoundId)
            if personID not in persons:
                persons[personID] = set()
            persons[personID].add(email)
        ans = []
        for personID, emailSet in persons.items():
            personName = accounts[personID][0]
            ans.append([personName] + sorted(list(emailSet)))
        return ans