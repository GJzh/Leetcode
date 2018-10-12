class Solution(object):
    class Person():
        def __init__(self, n):
            self.persons = [i for i in range(n)]
            self.jumps = [0] * n
        
        def find(self, k):
            cnt = 0
            while self.persons[k] != k:
                k = self.persons[k]
                cnt += 1
            self.jumps[k] = max(self.jumps[k], cnt)
            return k
        
        def merge(self, p1, p2):
            k1 = self.find(p1)
            k2 = self.find(p2)
            if self.jumps[k1] <= self.jumps[k2]:
                self.persons[k1] = k2
                return k2
            else:
                self.persons[k2] = k1
                return k1
                
    
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        if n == 0: return []
        p = self.Person(n)
        emails = {}
        for i in range(n):
            name = accounts[i][0]
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in emails:
                    emails[email] = i
                else:
                    emails[email] = p.merge(i, emails[email])
        persons = {}
        for email, idx in emails.items():
            ownerId = p.find(idx)
            if ownerId not in persons:
                persons[ownerId] = set()
            persons[ownerId].add(email)
        res = []
        for ownerId, emailList in persons.items():
            cur = [accounts[ownerId][0]]
            cur += sorted(list(emailList))
            res.append(cur)
        return res