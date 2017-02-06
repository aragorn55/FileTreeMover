'''
Created on Jan. 21 2017

@author: joshua meyer
'''
import sys
from file_tree_utility import FileTreeUtil
#ftool.move_files_of_exten(root, root_path_to_keep, destination, file_extension)
#ftool.move_files_of_exten(root,dest, r"/media/joshua/Data3/00FFSorted_by_exten", ".txt")
action = sys.argv[1]
sourceDir = sys.argv[2]
sourceRoot = sys.argv[3]
destination = sys.argv[4]
fileExtension = sys.argv[5]
def main():
    #ftool.move_files_of_exten(a, a, b, c)
    print("COMMAND ACTION SOURCE SOURCEROOT DESTINATION FILEEXTENSION")
    print("")
    if action == '-c':
        print("copying from" + sourceDir + "to" + destination)
        copy_tree(sourceDir, sourceRoot, destination, fileExtension)
    elif action == '-m':
        print("moving from" + sourceDir + "to" + destination)
        move_tree(sourceDir, sourceRoot, destination, fileExtension)



def copy_tree(source, root, dest, type):
    oTool = FileTreeUtil()
    oTool.copy_files_of_exten(source, root, dest, type)
    print("done")

def move_tree(source, root, dest, type):
    oTool = FileTreeUtil()
    oTool.move_files_of_exten(source, root, dest, type)
    print("done")

if __name__ == '__main__':
    main()