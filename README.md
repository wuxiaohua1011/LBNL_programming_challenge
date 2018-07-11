# LBNL Programming Challenge
## A. How to run this program:
1. open a terminal
2. type python myProgram.py --files [filename] --nodes [filename]



## B. Instruction:
### 1. Introduction
The goal of this challenge is to give you a chance to show how you would solve a small programming task, while at the same time give you a glimpse into the kind of problems we come across on a regular basis.
#### 1.1. Problem

You have a number of files of different size. You also have a number of compute nodes, with available space on their hard drives; the available space may also vary widely.

Your goal is to distribute the files as evenly as possible to the nodes.  One reason for doing this might be that you have a lot of clients reading these files, and you want to spread the load of these reads as evenly as possible across the nodes.

Note that it is the space used by the files, not the free space on the disk, that you are trying to balance. The free space is just a constraint on how much data you can fit onto the disk.
#### 1.2. Hints

1. Start with biggest files first, smallest ones last.
2. Try to put files on the node that has the least amount of data added so far.
3. Think about the data structures that will make it easier to access files and nodes in the order you want.
4. A perfect solution is not necessary. Try to get something reasonably good that can be achieved in a reasonable time, even for tens of thousands of files and hundreds of nodes.
5. Although a good solution is more important than beautiful code, please try to add reasonable comments and docstrings just as you would for a real Python program.  Consider your solution as something other people will use as part of a larger system.


### 2. Details
This section gives details on what the inputs will look like, what the outputs should look like, and how the program will be invoked from the command line.
#### 2.1. Inputs

There are two input files: `files.txt` and `nodes.txt`.  Both have the same
structure: simple text files, with one item per line, using the
newline character `\n` to separate lines. For both files, any blank line or line beginning with the comment character ('#') should be ignored. Any other line will have two fields separated by one or more spaces. The first field will be a string and the second field will be an integer:

 For `files`, the first field is the name of the file and the second field is the size of the file (in bytes).
 For `nodes`, the first field is the name of the node and the second field is the amount of free space (in bytes).

Example of "files.txt":

	# filename size  
	tom.dat 1024
	jerry.dat 16553
	tweety.out 12345
	elmerfudd.txt 987654321

Example of "nodes.txt":

	# node-name available-space
	node1 65536
	node2 32768
#### 2.2 Invocation
Your program should accept 2 flags: `--files <filename>` and `--nodes <filename>` to indicate the filenames of the input files. Consider using an argument parsing library for handling command-line flags (argparse, docopt, click etc.).
Eg.
python myprogram.py --files files.txt --nodes nodes.txt

#### 2.3. Output
The program should print its output to the terminal (i.e. standard output, the default for
the "print" statement). For each file, the output should have one line, with two fields separated by a space: the name of the file, and the  name of the node where it was placed by the program.
For files that didn't get placed on any node, use the word "NULL" for the node name.

Example of the output:

	tom.dat node1
	tweety.out node1
	jerry.dat node2
