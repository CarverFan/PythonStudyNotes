import os
import re
import time

# set the directory you want to start from
# note the forward-slash - this is the correct, cross-platform separator.
root_dir = "D:/recover"
working_list = []
unwanted = re.compile(r'(.*)(\.txt$|\.html$|\.h$|\.chm$|_dll$|_ocx$|\.ttf$|\.xml$|\.exe$|\.dll$|\.tff$|_exe$|_DLL$|_mui$|\.bat$|\.wim$|_MUI$|_sys$|\.java$|\.sqlite$|\.plist$|\.pf$|\.ico$|\.woff$|_expand$|_EXE$|\.ini$|\.cab$|\.reg)')

for dir_name, sub_dir_list, file_list in os.walk(root_dir):
    print(f'Checking directory: {dir_name}')
    for file in file_list:

        if unwanted.search(file):
            print(f'Unwanted File: {os.path.join(dir_name, file)} - deleting')
            os.remove(os.path.join(dir_name, file))
            continue

        if file in working_list:
            print(f'Deleting: {os.path.join(dir_name, file)}')
            os.remove(os.path.join(dir_name, file))
        else:
            working_list.append(file)

    # time.sleep(1)
print(working_list)
