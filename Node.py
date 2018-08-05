class Node:
    def __init__(self, nodeName, available_space, used_space=0):
        self.nodeName = nodeName
        self.available_space = available_space
        self.used_space = used_space
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return "nodeName: {} | available_space: {} | used_space: {}".format(self.nodeName, self.available_space, self.used_space)
    #for this.size < other.size
    def __lt__(self, other):
        return self.used_space < other.used_space if self.used_space != other.used_space else self.available_space < other.available_space
    # this.size <= other.size
    def __le__(self, other):
        return self.used_space <= other.used_space if self.used_space != other.used_space else self.available_space <= other.available_space
    # greater than
    def __gt__(self, other):
        return self.used_space > other.used_space if self.used_space != other.used_space else self.available_space > other.available_space
    def __ge__(self, other):
        return self.used_space >= other.used_space if self.used_space != other.used_space else self.available_space >= other.available_space
