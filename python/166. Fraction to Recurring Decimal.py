class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = sign + str(numerator / denominator)
        residual = numerator % denominator
        if residual == 0: return ans
        ans += "."
        visited = {}
        fractional = []
        while residual:
            if residual in visited:
                pos = visited[residual]
                return ans + "".join(fractional[:pos]) + "(" + "".join(fractional[pos:]) + ")"
            visited[residual] = len(fractional)
            residual *= 10
            val = residual / denominator
            fractional.append(str(val))
            residual %= denominator
        return ans + "".join(fractional)