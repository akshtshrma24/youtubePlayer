class Metrics:

    # Constructor

    def __init__(self):
        self.sent = False

    # sets sent value to is_sent

    def set_sent(self, is_sent):
        self.sent = is_sent

    # returns self.sent

    def get_sent(self):
        return self.sent
