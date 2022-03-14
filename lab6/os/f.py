#generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os

d = os.mkdir('folder to f.py')
path = 'folder to f.py'

for i in range(26):
    name = f'{chr(ord("A") + i)}.txt'
    file_path = os.path.join(path, name)
    files = open(file_path, 'w').close
    
