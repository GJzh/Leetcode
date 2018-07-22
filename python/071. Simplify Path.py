class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        myfiles = []
        i = 0
        while i < len(path):
            while i < len(path) and path[i] == '/': i += 1
            if i >= len(path): break
            file = ""
            while i < len(path) and path[i] != '/':
                file += path[i]
                i += 1
            if file == "..":
                if len(myfiles) > 0:
                    myfiles.pop()
            elif file != ".":
                myfiles.append(file)
        res = ""
        for file in myfiles:
            res += "/"
            res += file
        return res if res != "" else "/"

