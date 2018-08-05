### install and import packages
import pandas as pd
import argparse
from utility import arrange, File, Node


# commandline parser
parser = argparse.ArgumentParser()
parser.add_argument("--files", help='the path of the list of file name and size file', required= True)
parser.add_argument("--nodes", help='the path of the list of node name and available space file', required = True)

try:
    args = parser.parse_args()
except:
    parser.print_help()
    exit(1)

### read in data
file_name = args.files
node_name = args.nodes

file_df = None
nodes_df = None
try:
    files_df = pd.read_csv(file_name,comment="#", delim_whitespace=True, header=None)
    nodes_df = pd.read_csv(node_name,comment="#", delim_whitespace=True, header=None)
except:
    print("File import failed due to file not found. Example: python3 myProgram.py --files [fileName] --nodes [nodeFileName]")
    exit(1)

### reset colum names
files_df.columns=['filename','size']
nodes_df.columns=['nodes','available_space']

# put dataframe into array for sorting
files = []
nodes = []
for index, row in files_df.iterrows():
    f = File(row['filename'], row['size'])
    files.append(f)
for index, row in nodes_df.iterrows():
    n = Node(row['nodes'], row['available_space'])
    nodes.append(n)

result = arrange(files, nodes)

# print out result as required
for file in result:
    print(file)
