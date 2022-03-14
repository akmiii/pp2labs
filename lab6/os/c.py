#test whether a given path exists or not. If the path exist find the filename and directory portion of the given path

import os

path = input()
if os.path.exists(path):
    print(os.getcwd())
    if os.path.isdir(path):
        print(os.listdir(path))
    else:
        file = os.path.basename(path)
        print(file)
else:
    print("None")
