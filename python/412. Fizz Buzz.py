class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for num in range(1, n+1):
            if num % 15 == 0:
                cur = "FizzBuzz"
            elif num % 3 == 0:
                cur = "Fizz"
            elif num % 5 == 0:
                cur = "Buzz"
            else:
                cur = str(num)
            res.append(cur)
        return res