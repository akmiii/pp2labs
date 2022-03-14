#write a list to a file

l = input().split()
  
with open("example_2.txt", 'a') as f: #a - append
    for i in l:
        f.write(f'{i}\n')
    print("Success")
f.close()