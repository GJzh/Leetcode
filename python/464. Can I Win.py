class Solution(object):
    def _canIWin(self, maxChoosableInteger, desiredTotal, state):
        if desiredTotal <= 0: return False
        if state in self.status: return self.status[state]
        for num in range(maxChoosableInteger, 0, -1):
            if state & (1 << num): continue
            if not self._canIWin(maxChoosableInteger, desiredTotal-num, state | (1 << num)):
                self.status[state] = True
                return True
        self.status[state] = False
        return False
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= 1: return True
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger + 1) / 2: return False
        self.status = {}
        total = 0
        return self._canIWin(maxChoosableInteger, desiredTotal, 0)