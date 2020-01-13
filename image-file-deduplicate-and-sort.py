import os
from pathlib import Path
import shutil
import piexif

# set the directory you want to start from
# note the forward-slash - this is the correct, cross-platform separator.
root_dir = "C:/tmp/Dad Pics"
destination_dir = "C:/out"

for dir_name, sub_dir_list, file_list in os.walk(root_dir):
    print(f'Checking directory: {dir_name}')
    for file in file_list:

        # Extract the DateTimeOriginal data and split into year, month, day
        exif_dict = piexif.load(os.path.join(dir_name, file))
        for tag in exif_dict['Exif']:
            if piexif.TAGS['Exif'][tag]['name'] == 'DateTimeOriginal':
                # print(file, piexif.TAGS['Exif'][tag]['name'], exif_dict['Exif'][tag])
                dt = str(exif_dict['Exif'][tag]).split(':')
                year = dt[0].split(':')[0].split("'")[1]
                month = dt[1]
                day = dt[2].split()[0]
                print(f'date: {year}-{month}-{day}')
                directory = year + os.path.sep + month + os.path.sep + day

        # make the directory path
        Path(os.path.join(destination_dir, directory)).mkdir(parents=True, exist_ok=True)

        # copy the file
        print(f'Copying file {os.path.join(dir_name, file)} to {os.path.join(destination_dir, directory)}')
        try:
            done = shutil.copy(os.path.join(dir_name, file), os.path.join(destination_dir, directory))
        except OSError as why:
            print(f'Copy failed: {why}')
