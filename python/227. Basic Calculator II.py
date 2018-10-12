class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        part1 = 0
        part2 = 0
        idx = 0
        while idx < n and s[idx] == " ":
            idx += 1
        val = ""
        while idx < n and s[idx].isdigit():
            val += s[idx]
            idx += 1
        part2 = int(val)
        
        while idx < n:
            # ignore white spaces
            while idx < n and s[idx] == " ":
                idx += 1
            if idx >= n: return part1 + part2
            # get the operator
            operator = s[idx]
            idx += 1
            # ignore white spaces
            while idx < n and s[idx] == " ":
                idx += 1
            # get the value
            val = ""
            while idx < n and s[idx].isdigit():
                val += s[idx]
                idx += 1
            val = int(val)
            # update part1 and part2
            if operator == "+":
                part1, part2 = part1 + part2, val
            elif operator == "-":
                part1, part2 = part1 + part2, -val
            elif operator == "*":
                part1, part2 = part1, part2 * val
            elif operator == "/":
                sign = 1 if part2 >= 0 else -1
                part1, part2 = part1, abs(part2) / val * sign
            else: return 0

        return part1 + part2