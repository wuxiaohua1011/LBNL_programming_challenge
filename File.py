class File:
    def __init__(self, filename, size, storage_node=None):
        self.filename = filename
        self.size = size
        self.storage_node = None
    def __str__(self):
        return "{} {}".format(self.filename, "Null" if self.storage_node == None else self.storage_node.nodeName)
    def __repr__(self):
        return "filename: {} | size: {} | storage_node: {}".format(self.filename, self.size, "Null" if self.storage_node == None else self.storage_node.nodeName)
    #for this.size < other.size
    def __lt__(self, other):
        return self.size < other.size
    # this.size <= other.size
    def __le__(self, other):
        return self.size <= other.size
    # greater than
    def __gt__(self, other):
        return self.size > other.size
    def __ge__(self, other):
        return self.size >= other.size
    # add the node to storage node and return true, return false if cannot add
    def addNode(self, node):
        if node.available_space >= self.size:
            node.available_space = node.available_space - self.size
            node.used_space = self.size + node.used_space
            self.storage_node = node
            return True
        else:
            return False
    
