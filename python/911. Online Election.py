class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        votes = [(times[i], persons[i]) for i in range(len(times))]
        self.wins = []
        self.candidates = {}
        t = times[0]
        cnt = 0
        winner = -1
        for i in range(len(times)):
            person, time = persons[i], times[i]
            if time != t: 
                self.wins.append((t, winner))
                t = time
            if person not in self.candidates:
                self.candidates[person] = 1
            else:
                self.candidates[person] += 1
            if self.candidates[person] >= cnt:
                winner = person
                cnt = self.candidates[person]
        self.wins.append((t, winner))

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        left, right = 0, len(self.wins)-1
        while left <= right:
            mid = (left + right) / 2
            if self.wins[mid][0] <= t:
                left = mid + 1
            else:
                right = mid - 1
        return self.wins[right][1]