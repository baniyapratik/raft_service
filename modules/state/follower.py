from .voter import Voter


class Follower(Voter):

    def __init__(self, timeout=500):
        Voter.__init__(self)
        self._timeout = timeout
        self._timeoutTime = self._nextTimeout()


