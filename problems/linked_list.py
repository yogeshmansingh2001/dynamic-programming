class Node:
    data  = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node Data : %s>" %self.data