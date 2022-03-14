#copy the contents of a file to another file

with open("example_2.txt", 'r') as f:
    with open('text.txt', 'w') as c_f:
        for words in f:
            c_f.write(words)
    c_f.close()