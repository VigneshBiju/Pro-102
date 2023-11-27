import os
import shutil

from_dir= C: \Users\User\Documents\Project 102C
to_dir= C: \Users\User\Documents\Document_files

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in os.listdir(list_of_files):
    name, ext = os.path.splitext(file)

    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        