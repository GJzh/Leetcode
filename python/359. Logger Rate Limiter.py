class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.status = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.status:
            self.status[message] = timestamp
            return True
        else:
            if timestamp - self.status[message] >= 10:
                self.status[message] = timestamp
                return True
            else:
                return False