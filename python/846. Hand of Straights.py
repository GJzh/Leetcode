class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if (n % W): return False
        cards = {}
        for card in hand:
            if card not in cards:
                cards[card] = 1
            else:
                cards[card] += 1
        q = cards.items()
        heapq.heapify(q)
        for k in range(n / W):
            temp = []
            if len(q) < W: return False
            for i in range(W):
                if i > 0 and q[0][0] != temp[-1][0] + 1: return False
                temp.append(q[0])
                heapq.heappop(q)
            
            for card, cnt in temp:
                if cnt > 1:
                    heapq.heappush(q, (card, cnt-1))
        return len(q) == 0