import pandas as pd
from heapq import heappush, heappop
import argparse
import heapq
from File import File
from Node import Node
# sorting algorithm
######################################################################################################################################################
# DESCRIPTION:
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
####################################################################################################################################################
def arrange(files, nodes):
    ### inplace heapification
    heapq._heapify_max(files)
    heapq._heapify_max(nodes)
    result = []
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
    return result
