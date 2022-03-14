#list only directories, files and all directories, files in a specified path

import os

path = input() #pp2labs\lab3
l = []
dir = []
files = []
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        dir.append(os.path.join(dirpath, dirname)) #to print 'lab3\\function1\\__pycache__'
        l.append(dirname)
    for file in filenames:
        files.append(os.path.join(dirpath, file))
        l.append(file)
print(f'Directories: {dir}\nFiles: {files}\nDirectories and Files: {l}')

