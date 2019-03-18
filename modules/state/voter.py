class Voter():

    def __init__(self):
        self.voted = False
        self.voted_to = None

    def vote_request(self, message):
        if self.voted:
            self._send_vote_message(vote=False)
        else:
            self._send_vote_message(message, vote=True) # vote for the leader
            self.voted_to = message.sender
            self.voted = True # change the status of voted
