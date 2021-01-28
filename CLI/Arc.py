# class for arcs

class Arc:
    """docstring for Arc."""

    def __init__(self, name):
        self.name = name
    def initialize(self, frm, to, status):
        self.frm = frm
        self.to = to
        self.status = status
