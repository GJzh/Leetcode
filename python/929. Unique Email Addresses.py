class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        visited = {}
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            email = local + "@" + domain
            if email not in visited:
                visited[email] = True
        return len(visited)