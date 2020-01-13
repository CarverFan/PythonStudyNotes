import os
from pathlib import Path
import shutil
import piexif
import platform
from datetime import datetime

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        x = os.path.getmtime(path_to_file)
        date_mod_time = datetime.fromtimestamp(x).strftime("%Y, %m, %d")
        return date_mod_time
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

root_dir = "D:/temp_mov_files"
destination_dir = "C:/out"

for dir_name, sub_dir_list, file_list in os.walk(root_dir):
    print(f'Checking directory: {dir_name}')
    for file in file_list:

        date_mod_time = creation_date(os.path.join(dir_name, file))
        dmt = date_mod_time.split(',')
        year, month, day = dmt
        directory = year + os.path.sep + month + os.path.sep + day
        #print(f'date_mod: {time.strftime("%Y, %m, %d", )}')

        # make the directory path
        Path(os.path.join(destination_dir, directory)).mkdir(parents=True, exist_ok=True)

        # copy the file
        print(f'Copying file {os.path.join(dir_name, file)} to {os.path.join(destination_dir, directory)}')
        try:
            done = shutil.copy(os.path.join(dir_name, file), os.path.join(destination_dir, directory))
        except OSError as why:
            print(f'Copy failed: {why}')
