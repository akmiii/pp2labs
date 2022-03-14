#delete file by specified path. Before deleting check for access and whether a given path exists or not

import os

path = input()
if os.path.exists(path):
    os.remove(path)
    print("Success")
else:
    print("None")