### install and import packages
import pandas as pd
from heapq import heappush, heappop
import heapq, argparse
# commandline parser
parser = argparse.ArgumentParser()
parser.add_argument("--files", help='the path of the list of file name and size file')
parser.add_argument("--nodes", help='the path of the list of node name and available space file')
args = parser.parse_args()
### read in data
file_name = args.files
node_name = args.nodes
files_df = pd.read_csv(file_name,comment="#", delim_whitespace=True, header=None)
nodes_df = pd.read_csv(node_name,comment="#", delim_whitespace=True, header=None)
### reset colum names
files_df.columns=['filename','size']
nodes_df.columns=['nodes','available_space']
### define customized data objects
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

# put dataframe into array for sorting
files = []
nodes = []
for index, row in files_df.iterrows():
    f = File(row['filename'], row['size'])
    files.append(f)
for index, row in nodes_df.iterrows():
    n = Node(row['nodes'], row['available_space'])
    nodes.append(n)

### inplace heapification
heapq._heapify_max(files)
heapq._heapify_max(nodes)

# initialize a result list for storing results
result = []
# as long as there are still files in the heap
# pop off the first element in the file heap, call it current_file
# pop off the first element in the nodes heap, call it current_node
# if current_file add current_node is successful
#     check if the node still have space
#         if yes, push the node back to the nodes heap
# else(current_file cannot be stored in current_node)
#     as long as there are still node in the nodes heap
#         push the current node to a temporary list used to push the the current node back onto the heap
#         pop off the first node, set current_node to that node
#         if current_file can add current_node, break, otherwise, continue
#     if there are no nodes that can store this file, this file just simply would not be modified, and the field of storage node will be None
#     re-heapify nodes
# append the current_file to the list of result
while files:
    current_file = heapq.heappop(files)
    temp_nodes = []
    current_node = heapq.heappop(nodes)
    if not current_file.addNode(current_node):
        while(nodes):
            temp_nodes.append(current_node)
            current_node = heapq.heappop(nodes)
            if current_file.addNode(current_node):
                break
        nodes = nodes + temp_nodes
        heapq._heapify_max(nodes)
        temp_nodes = []

    if current_node.available_space > 0:
        heapq.heappush(nodes, current_node)
    result.append(current_file)

# print out result as required
for file in result:
    print(file)
