#!/usr/bin/python
from file_tree_utility import FileTreeUtil

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

ftool = FileTreeUtil()
root = r"/media/joshua/Data3/all_ff_stuff"
dest = r"/media/joshua/Data3/ff_by_type"
a = r"/media/joshua/Data3/0FileTypes"
b = r"/media/joshua/Data3/0FileTypes/0Ark/0Tar"
c = r".tar"
d = r""
rb = r""
exten = ".html"
#ftool.move_files_of_exten(root, root_path_to_keep, destination, file_extension)
#ftool.move_files_of_exten(root,dest, r"/media/joshua/Data3/00FFSorted_by_exten", ".txt")
ftool.move_files_of_exten(a, a, b, c)
