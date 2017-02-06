import os
import shutil as sh
import re
from unipath import Path
class FileTreeUtil(object):

    def copy_files_of_exten(self, root, root_path_to_keep, destination, file_extension):

        #root_path = "./folder_A"
        #dest_path = "./folder_B"

        self.transfer_files_by_exren(destination, file_extension, root, root_path_to_keep)

    # Defaults to copying files add a false at the end to move them
    def transfer_files_by_exren(self, destination, file_extension, root, root_path_to_keep, copy_files=True):
        root_path = root
        dest_path = Path(destination)
        dest_path.mkdir(parents=True)
        file_exten = file_extension
        old_path = root_path_to_keep
        for dirpath, dnames, fnames in os.walk(root_path):
            for f in fnames:
                newf = ''
                if f.endswith(file_exten):
                    oldf = Path(dirpath, f)
                    new_file = self.get_new_path(oldf, old_path, dest_path)
                    print(new_file)
                    self.create_dest_folder(new_file)
                    oldf = Path(dirpath, f)
                    print(oldf)
                    if copy_files:
                        oldf.copy(new_file)
                    else:
                        oldf.move(new_file)

    def move_files_of_exten(self, root, root_path_to_keep, destination, file_extension):

        self.transfer_files_by_exren(destination, file_extension, root, root_path_to_keep, copy_files=False)

    def get_new_path(self, oldFilePath, oldPathRoot, newPathRoot):
        oldPath = Path(oldFilePath)
        oldRoot = Path(oldPathRoot)
        newRoot = Path(newPathRoot)
        fileName = oldPath.name
        oldFolder = oldPath.parent
        oldFolders = oldFolder.components()
        oldrootcnt = len(oldRoot.components())
        newpathlist = oldFolders[oldrootcnt -1:]
        if len(newpathlist) > 0:
            newPath = Path(newPathRoot, newpathlist, fileName)
        else:
            newPath = Path(newPathRoot, fileName)
        if newPath.exists():
            newPath = self.get_path_collide(newPath)
        else:
            pass

        return newPath

    def create_dest_folder(self, file):
        folder = file.parent
        folder.mkdir(parents=True)

    def get_path_collide(self, filepath, startcnt=1):
        root = filepath.parent
        exten = filepath.ext
        file = filepath.stem
        fixed = ""
        startcnt = 1
        pattern = re.compile(r'\(\d+\)$')
        match = pattern.search(file)
        if match:
            match_cnt = len(match.groups())
            if match_cnt == 0:
                fixed = self.parse_match(exten, file, match, root)
            else:
                result = match.groups()[match_cnt -1]
                fixed = self.parse_match(exten, file, result, root)

        else:
            fixed = self.new_filename(startcnt, file, exten, root)

        return fixed

    def parse_match(self, exten, file, match, root):
        s = match.start()
        e = match.end()
        dup_cnt = file[s + 1:e - 1]
        basename = file[s:]
        idupcnt = int(dup_cnt)
        fixed = self.new_filename(idupcnt, basename, exten, root)
        return fixed

    def new_filename(self, filecnt, newname, exten, root):
        newfile = newname + "(" + str(filecnt) + ")"+ exten
        newfilename = Path(root, newfile)
        exists = newfilename.exists()
        if exists:
            new_filename = self.new_filename(filecnt + 1, newname, exten, root)
        else:
            return newfilename
        return new_filename

    def RepresentsInt(s):
        try:
            int(s)
            return True
        except ValueError:
            return False




